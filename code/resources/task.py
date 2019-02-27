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


  # POST 
  def post(self):
    data = Task.parser.parse_args()
    task = TaskModel.find_by_name(data['task_name'])
    if task:
      return { "error": "The task already exists" }, 500
      # task.task_description = data['task_description']
      # task.instructor_id = data['instructor_id']
      # task.task_notes = data['task_notes']
  
    else:
      task = TaskModel(
        data['task_name'], 
        data['task_description'], 
        data['instructor_id'],
        data['task_notes'])

    try:
      task.save_to_db()
    except:
      return { "message": "An error occurred inserting the task" }, 500

    return task.json(), 201
  



  # PUT (taskname) ----------------
  def put(self):
    data = Task.parser.parse_args()
    task = TaskModel.find_by_name(data['task_name'])

    # If task exists, edit
    if task:
      task.task_description = data['task_description']
      task.instructor_id = data['instructor_id']
      task.task_notes = data['task_notes']

    # If task doesn't ecist, create new task
    else:
      task = TaskModel(data['task_name'],
        data['task_description'],
        data['instructor_id'],
        data['task_notes'])

    task.save_to_db()
    return task.json()



  # DELETE 
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
  

  parser = reqparse.RequestParser()
  parser.add_argument('task_name',
    type = str)
  parser.add_argument('task_description',
    type = str)
  parser.add_argument('task_notes',
    type = str)
  parser.add_argument('instructor_id',
    type = int)


  # POST
  def post(self):
    if TaskModel.find_by_description('task_description'):
      return {'message': "A task with that description already exists"}, 400

    data = NewTask.parser.parse_args()
    newTask = TaskModel(
      data['task_name'],
      data['task_description'],
      False,
      '', 
      '', 
      data['instructor_id'],
      data['task_notes'])
    
    try:
      newTask.save_to_db()

    except:
      return {'message': "An error occured inserting the task"}, 500

    return  newTask.json(), 201