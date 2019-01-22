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
  #region
  def get(self, _id):
    position = PositionModel.find_by_id(_id)
    if position:
      return position.json_task()
    return {'message': 'Position not found'}, 404
  #endregion


  # GET (templateid)
  #region
  # def get(self, templateid):
  #   position = PositionModel.find_by_template(templateid)
  #   # print(len(position))
  #   if position:
  #     return {'positions': [position.json_task() for position in position]}
  #     # return position.json()
  #   return {'message': 'Position not found'}, 404
  #endregion

 
  # POST(_id)
  #region
  def post(self, _id):
    if PositionModel.find_by_id(_id):
      return {'message': "A position with this id already exists"}, 400

    data = Position.parser.parse_args()
    # print(data)
    position = PositionModel(data['template_id'], 
      data['task_id'], 
      data['position_no'])

    try:
      position.save_to_db()

    except:
      return {"message": "An error occured inserting the position"}, 500

    return position.json(),201
  #endregion



  def put(self, positionname):
    pass

   
  def delete(self, positionname):
    pass
 


class Positions(Resource):
  def get(self):
    return {'positions': [position.json_task() for position in PositionModel.query.all()]}


