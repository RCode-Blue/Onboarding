from flask_restful import Resource, reqparse
from models.task import TaskModel
from datetime import datetime

class Task(Resource):
  #region
  parser = reqparse.RequestParser()
  parser.add_argument('task_id',
    type = int)
  parser.add_argument('task_name',
    type = str)
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
  #endregion

  # GET 
  def get(self):
    data = Task.parser.parse_args()
    task = TaskModel.find_by_id(data['task_id'])
    if task:
      return task.json()
    return {'message': 'Task not found'}, 404


  # POST (create new)
  def post(self):
    data = Task.parser.parse_args()
    task = TaskModel.find_by_description(data['task_description'])
    if task:
      return { "error": "The task already exists" }, 500

    else:
      newTask = TaskModel(
        data['task_name'],
        data['task_description'],
        data['instructor_id'],
        data['task_notes'])

    try:
      newTask.save_to_db()
    except:
      return { "message": "An error occurred inserting the task" }, 500

    return newTask.json(), 201
  

  # PUT (edit) (task_name)
  def put(self):
    data = Task.parser.parse_args()
    task = TaskModel.find_by_name(data['task_name'])

    # If task exists, edit
    if task:
      task.task_description = data['task_description']
      task.instructor_id = data['instructor_id']
      task.task_notes = data['task_notes']

      task.save_to_db()

      return task.json()

    # If task doesn't exist, create new
    else:
      newTask = TaskModel(
        data['task_name'],
        data['task_description'],
        data['instructor_id'],
        data['task_notes'])

      newTask.save_to_db()
      return newTask.json()


  # DELETE (task_id)
  def delete(self):
    data = Task.parser.parse_args()
    task = TaskModel.find_by_name(data['task_name'])
    if task:
      task.delete_from_db()
      return {"message": "Task deleted"}

    return {"message": "Task not found"}, 400




class Tasks(Resource):
  def get(self):
    return {"tasks": [task.json() for task in TaskModel.query.all()]}
  


