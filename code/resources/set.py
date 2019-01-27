from flask_restful import Resource, reqparse
from models.set import SetModel
from models.sequence import SequenceModel

class Set(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('template_id',
    type = int)
  parser.add_argument('description',
    type = str)
  parser.add_argument('city',
    type = str)
  parser.add_argument('start_date',
    type = str)
  parser.add_argument('employee_id',
    type = int)
  parser.add_argument('manager_id',
    type = int)
  parser.add_argument('buddy_id',
    type = int)
  

  # GET(id)
  #region
  def get(self, _id):
    set = SetModel.find_by_id(_id)
    if set:
      return set.json_template()
    return {'message': 'Set not found'}, 404
  #endregion


  # POST

  # DELETE

  # PUT



class Sets(Resource):
  def get(self):
    return {"sets": [set.json() for set in SetModel.query.all()]}


class AddSequence(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('sequence_id',
    type = int)

  # PUT
  def put(self, _id):
    data = AddSequence.parser.parse_args()

    # Get the Set
    set = SetModel.find_by_id(_id)
    if set:
      if (set.sequence_id):
        return {'message': 'This set is already allocated'}, 400
      else:
        SetModel.create_new_sequence(_id, set, data)

    else:
      return {'error': 'The Set does not exist'}, 400



    # return set.json()
