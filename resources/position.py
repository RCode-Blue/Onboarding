from flask import jsonify, request
from flask_restful import Resource, reqparse
from models.position import PositionModel


class Position(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("position_id", type=int)
    parser.add_argument("template_id", type=int)
    parser.add_argument("task_id", type=int)
    parser.add_argument("position_no", type=int)

    # GET (id)
    def get(self):
        data = Position.parser.parse_args()
        position = PositionModel.find_by_id(data["position_id"])
        if position:
            return position.json_task()
        return {"message": "Position not found"}, 404

    # PUT
    def put(self):
        data = Position.parser.parse_args()
        if PositionModel.find_by_position(
            data["template_id"], data["task_id"], data["position_no"]
        ):
            return (
                {
                    "message": "This position has already been allocated to this template"
                },
                500,
            )

        position = PositionModel(
            data["template_id"], data["task_id"], data["position_no"]
        )

        try:
            position.save_to_db()
            return position.json(), 201
        except:
            return {"message": "An error occured inserting the position"}, 500

    # POST (create)
    def post(self):
        data = Position.parser.parse_args()
        if PositionModel.find_by_position(
            data["template_id"], data["task_id"], data["position_no"]
        ):
            return {"message": "A position with this name already exists"}, 400

        position = PositionModel(
            data["template_id"], data["task_id"], data["position_no"]
        )

        try:
            position.save_to_db()
        except:
            return {"message": "An error occured editing the position"}, 500

        return position.json(), 201

    # DELETE
    def delete(self):
        data1 = Position.parser.parse_args()

        position = PositionModel.find_by_id(data1["position_id"])
        if position:
            position.delete_from_db()
            return {"message": "Position deleted"}

        return {"error": "Position does not exist"}, 500


class Positions(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("positions", type=list, location="json")

    def get(self):
        return {
            "positions": [
                position.json_task() for position in PositionModel.query.all()
            ]
        }

    def put(self):
        data = Positions.parser.parse_args()

        json_data = request.get_json(force=True)
        positions = json_data["positions"]

        for position in positions:
            if position["position_no"] != position["prev_position_no"]:
                matched_position = PositionModel.find_by_id(position["position_id"])

                if matched_position:
                    matched_position.position_no = position["position_no"]

                    matched_position.save_to_db()
                    return {"edited_position": matched_position.json()}, 201

                # If task doesn't exist, error out
                else:
                    return {"message": "Position does not exist"}, 404

