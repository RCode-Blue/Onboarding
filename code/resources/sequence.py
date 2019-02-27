from flask_restful import Resource, reqparse
from models.sequence import SequenceModel

class Sequence(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('set_id', 
    type = int)
  parser.add_argument('task_description',
    type = str)
  parser.add_argument('task_position',
    type = int)
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

  
  # PUT (modify)
  def put(self):
    data = Sequence.parser.parse_args()
    sequence = SequenceModel.find_by_task_description(data['task_description'])

    # If sequence item exists, error out
    if sequence:
      return {"error": "The specified task already exists"}, 500
    # Otherwise, add new sequence item
    else:
      sequence = SequenceModel(
        data['set_id'],
        data['task_description'],
        data['task_position'],
        data['completed'],
        data['completion_date'],
        data['checked_off_by'],
        data['instructor_id'],
        data['task_notes'])
    
    sequence.save_to_db()
    # return sequence.json()



  # DELETE
  def delete(self, _id):
    sequence = SequenceModel.find_by_name(_id)
    if sequence:
      sequence.delete_from_db()

    return{"message": "Sequence deleted"}



class Sequences(Resource):
  def get(self):
    return {'sequences': [sequence.json() for sequence in SequenceModel.query.all()]}





class TaskList(Resource):
  # parser = reqparse.RequestParser()
  # parser.add_argument('set_id', 
  #   type = int)

  def get(self, set_id):
    # pass
    tasks = SequenceModel.find_by_set_id(set_id)
    if tasks:
      # return {'message': 'Tasks found'}
      # print(tasks)
      return {'tasks': [task.json() for task in tasks]}
    else:
      return {'message': 'No task found'}
    # return {'tasks': [task.json() for task in tasks]}


