from flask_restful import Resource, reqparse
from models.position import PositionModel

class Position(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('position_id',
    type = int)
  parser.add_argument('template_id',
    type = int)
  parser.add_argument('task_id',
    type = int)
  parser.add_argument('position_no',
    type = int)


  # GET (id)
  def get(self):
    data = Position.parser.parse_args()
    position = PositionModel.find_by_id(data['position_id'])
    if position:
      return position.json_task()
    return {'message': 'Position not found'}, 404


  # PUT
  def put(self):
    data = Position.parser.parse_args()
    # position = PositionModel.find_by_position(data['template_id'], data['task_id'], data['position_no'])
    if PositionModel.find_by_position(data['template_id'], data['task_id'], data['position_no']):
    # if position:
      # return position.json()
      return {"message": "This position has already been allocated to this template"}, 500

    position = PositionModel(
      data['template_id'],
      data['task_id'],
      data['position_no'])
    
    try:
      position.save_to_db()
      return position.json(), 201
    except:
      return {"message": "An error occured inserting the position"}, 500


  # POST (create)
  def post(self):
    data = Position.parser.parse_args()
    if PositionModel.find_by_position(data['template_id'], data['task_id'], data['position_no']):
      return {'message': "A position with this name already exists"}, 400

    data = Position.parser.parse_args()
    position = PositionModel(
      data['template_id'], 
      data['task_id'], 
      data['position_no'])

    try:
      position.save_to_db()
    except:
      return {"message": "An error occured editing the position"}, 500

    return position.json(),201


  # DELETE
  def delete(self):
    data = Position.parser.parse_args()
    position = PositionModel.find_by_id(data['position_id'])
    if position:
      position.delete_from_db()
    
      return {"message": "Position deleted"}

    return{"error": "Position does not exist"}, 500
 


class Positions(Resource):
  def get(self):
    return {'positions': [position.json_task() for position in PositionModel.query.all()]}





