from flask_restful import Resource, reqparse
from models.sequence import SequenceModel

class Sequence(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('sequence_name',
    type = str
  )
  parser.add_argument('sequence_description',
    type = str
  )


  def get(self, sequencename):
    sequence = SequenceModel.find_by_name(sequencename)
    if sequence:
      return sequence.json()
    return {'message': 'Sequence not found'}, 404


  def post(self, sequencename):
    if SequenceModel.find_by_name(sequencename):
      return {'message': 'A sequence with that name already exists'}

    data = Sequence.parser.parse_args()
    print(data)
    sequence = SequenceModel(sequencename, data['sequence_description'])
    # sequence = SequenceModel(sequencename, **data)

    try:
      sequence.save_to_db()
    except:
      return {"message":
              "An error occured inserting this sequence"}, 500

    return sequence.json(), 201


  def delete(self, sequencename):
    sequence = SequenceModel.find_by_name(sequencename)
    if sequence:
      sequence.delete_from_db()

    return{"message": "Sequence deleted"}


  def put(self, sequencename):
    data = Sequence.parser.parse_args()
    sequence = SequenceModel.find_by_name(sequencename)

    if sequence is None:
      sequence = SequenceModel(sequencename, data['sequence_description'])

    else:
      sequence.sequence_description = data['sequence_description']

    sequence.save_to_db()
    return sequence.json()

class Sequences(Resource):
  def get(self):
    return {'sequences': [sequence.json() for sequence in SequenceModel.query.all()]}


  
class SequenceTasks(Resource):
  def get(self, sequencename):
    sequence = SequenceModel.find_by_name(sequencename)
    if sequence:
      

      return sequence.json()



    return {'message': 'Sequence not found'}, 404




