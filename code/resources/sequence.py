from flask_restful import Resource, reqparse
from models.sequence import SequenceModel

class Sequence(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('set_id', 
    type = int)
  parser.add_argument('task_description',
    type = str)
  parser.add_argument('completed',
    type = bool)
  parser.add_argument('completion_date',
    type = str)
  parser.add_argument('checked_off_by',
    type = int)
  parser.add_argument('instructor_id',
    type = int)
  parser.add_argument('task_notes',
    type = str)


  # GET
  def get(self, _id):
    sequence = SequenceModel.find_by_id(_id)
    if sequence:
      # return sequence.json()
      return sequence.json_positions()
    return {'message': 'Sequence not found'}, 404


  # POST
  def post(self, _id):
    if SequenceModel.find_by_name(_id):
      return {'message': 'A sequence with that name already exists'}

    data = Sequence.parser.parse_args()
    print(data)
    sequence = SequenceModel(_id, data['sequence_description'])
    # sequence = SequenceModel(sequencename, **data)

    try:
      sequence.save_to_db()
    except:
      return {"message":
              "An error occured inserting this sequence"}, 500

    return sequence.json(), 201


  # DELETE
  def delete(self, _id):
    sequence = SequenceModel.find_by_name(_id)
    if sequence:
      sequence.delete_from_db()

    return{"message": "Sequence deleted"}


  # PUT
  # def put(self, _id):
  #   data = Sequence.parser.parse_args()
  #   sequence = SequenceModel.find_by_id(_id)

  #   if sequence is None:
  #     sequence = SequenceModel(_id, 
  #       data['set_id'],
  #       '','','','','')

  #   else:
  #     sequence.set_id = data['set_id']

  #   sequence.save_to_db()
  #   return sequence.json()



class Sequences(Resource):
  def get(self):
    return {'sequences': [sequence.json() for sequence in SequenceModel.query.all()]}


  



