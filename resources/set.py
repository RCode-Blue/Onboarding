from flask_restful import Resource, reqparse
from models.set import SetModel
from models.sequence import SequenceModel
from models.template import TemplateModel

import datetime


class Set(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("_id", type=int)
    parser.add_argument("template_id", type=int)
    parser.add_argument("description", type=str)
    parser.add_argument("city", type=str)
    parser.add_argument("start_date_year", type=str)
    parser.add_argument("start_date_month", type=str)
    parser.add_argument("start_date_date", type=str)
    parser.add_argument("employee_id", type=int)
    parser.add_argument("manager_id", type=int)
    parser.add_argument("buddy_id", type=int)
    parser.add_argument("sequence_id", type=int)

    # GET(id)

    def get(self):
        data = Set.parser.parse_args()
        _set = SetModel.find_by_id(data["_id"])
        if _set:
            return _set.json_template()
        return {"message": "Set not found"}, 404

    # POST (create)
    def post(self):
        data = Set.parser.parse_args()

        formatted_start_date = datetime.date(
            int(data["start_date_year"]),
            int(data["start_date_month"]),
            int(data["start_date_date"]),
        )

        _set = SetModel.find_by_set(
            templateid=data["template_id"], employeeid=data["employee_id"]
        )

        if _set:
            return {"message": "This employee has already been allocated this template"}

        new_set = SetModel(
            data["template_id"],
            data["description"],
            data["city"],
            formatted_start_date,
            data["employee_id"],
            data["manager_id"],
            data["buddy_id"],
        )

        try:
            new_set.save_to_db()
            return {"newSet": new_set.json()}
        except:
            return {"message": "An error occured creating the set"}, 500

    # PUT (edit)
    def put(self):
        data = Set.parser.parse_args()
        _set = SetModel.find_by_set(data["template_id"], data["employee_id"])
        if _set:
            _set = SetModel(
                data["template_id"],
                data["description"],
                data["city"],
                data["start_date"],
                data["employee_id"],
                data["manager_id"],
                data["buddy_id"],
            )

        try:
            _set.save_to_db()
            return _set.json()
        except:
            return {"message": "An error occured inserting the set"}, 500

    # DELETE


class Sets(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("employee_id", type=int)

    def get(self):
        data = Sets.parser.parse_args()
        sets = SetModel.find_by_user_id(data["employee_id"])

        return {"sets": [set.json() for set in sets]}


class AddSequence(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("set_id", type=int)

    # POST
    def post(self, set_id):
        data = AddSequence.parser.parse_args()

        # Get the Set
        set = SetModel.find_by_id(set_id)
        # If set exists...
        if set:
            # ...and it already has an associated sequence, return error message
            if set.allocated:
                return {"message": "This set is already allocated"}, 400
            # Otherwise create new sequence
            SetModel.create_new_sequence(set_id, set, data)
            return {set: set.json()}

        else:
            return {"error": "The Set does not exist"}, 404

        assigned_template = TemplateModel.find_by_id(set.template_id)
        return {"assigned_tempplate": assigned_template.json()}
