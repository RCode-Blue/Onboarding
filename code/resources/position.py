from flask_restful import Resource, reqparse
from models.position import PositionModel

class Position(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('template_id',
    type = int)
  parser.add_argument('task_id',
    type = int)
  parser.add_argument('position_no',
    type = int)

  # parser.add_argument('completed',
  #   type = bool)
  # parser.add_argument('completion_date',
  #   type = str)

  # GET (positionname)
  #region
  # def get(self, positionname):
  #   position = PositionModel.find_by_name(positionname)
  #   # print('-------------------')
  #   # print(position.task_id)
  #   if position:
  #     return position.json_task()
  #   return {'message': 'Position not found'}, 404
  #endregion


  # GET (id)
  # def get(self, id):
  #   position = PositionModel.find_by_id(id)
  #   if position:
  #     return position.json_task()
  #   return {'message': 'Position not found'}, 404
 

  def get(self, templateid):
    position = PositionModel.find_by_template(templateid)
    # print(position)
    if position:
      return position.json()
    return {'message': 'Position not found'}, 404



  # GET (template_id, task_id, position_no)

  def post(self, templateid):
    data = Position.parser.parse_args()
    print(data)

  def put(self, positionname):
    pass

   
  def delete(self, positionname):
    pass



class Positions(Resource):
  def get(self):
    return {'positions': [position.json_task() for position in PositionModel.query.all()]}


