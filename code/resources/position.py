from flask_restful import Resource, reqparse
from models.position import PositionModel

class Position(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('position_name',
    type = str
    )
  parser.add_argument('task_id',
    type = int
    )
  parser.add_argument('sequence_id',
    type = int
    )
  parser.add_argument('sequence_no',
    type = int
    )

  def get(self, positionname):
    position = PositionModel.find_by_name(positionname)
    # print('-------------------')
    # print(position.task_id)
    if position:
      return position.json_task()
    return {'message': 'Position not found'}, 404





  def post(self, positionname):
    pass



  def delete(self, positionname):
    pass




  def put(self, positionname):
    pass


class Positions(Resource):
  def get(self):
    return {'positions': [position.json() for position in PositionModel.query.all()]}


