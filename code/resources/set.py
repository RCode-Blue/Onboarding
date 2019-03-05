from flask_restful import Resource, reqparse
from models.set import SetModel
from models.sequence import SequenceModel

class Set(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('_id', type = int)
  parser.add_argument('template_id', type = int)
  parser.add_argument('description', type = str)
  parser.add_argument('city', type = str)
  parser.add_argument('start_date', type = str)
  parser.add_argument('employee_id', type = int)
  parser.add_argument('manager_id', type = int)
  parser.add_argument('buddy_id', type = int)
  parser.add_argument('sequence_id', type = int)
  

  # GET(id)
  def get(self):
    data = Set.parser.parse_args()
    set = SetModel.find_by_id(data['_id'])
    if set:
      return set.json_template()
      # return set.json()
    return {'message': 'Set not found'}, 404


  # PUT (edit)
  def put(self):
    data = Set.parser.parse_args()
    set = SetModel.find_by_set(data['template_id'], data['employee_id'])
    if set:
      set = SetModel(
        data['template_id'],
        data['description'],
        data['city'],
        data['start_date'],
        data['employee_id'],
        data['manager_id'],
        data['buddy_id']
      )

    try:
      set.save_to_db()
      return set.json()
    except:
      return {"message": "An error occured inserting the set"}, 500

    

  # POST (create)
  def post(self):
    pass


  # DELETE






class Sets(Resource):
  def get(self):
    return {"sets": [set.json() for set in SetModel.query.all()]}


class AddSequence(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('set_id',
    type = int)

  # POST
  def post(self, set_id):
    data = AddSequence.parser.parse_args()

    # Get the Set
    set = SetModel.find_by_id(set_id)
    # If set exists...
    if set:
      # ...and it already has an associated sequence, return error message
      # if (set.sequence_id):
      if (set.allocated):
        # return {'message': 'This set is already allocated'}, 400
        return set.json()
      # Otherwise create new sequence
      
      SetModel.create_new_sequence(set_id, set, data)
      return set.json()

    else:
      return {'error': 'The Set does not exist'}, 400



    # return set.json()