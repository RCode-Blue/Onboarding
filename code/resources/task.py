from flask_restful import Resource, reqparse
from models.task import TaskModel
from datetime import datetime

class Task(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('task_name',
    type = str
    )
  parser.add_argument('task_description',
    type = str
    )
  parser.add_argument('completed',
    type = bool
    )
  parser.add_argument('completion_date'
    )
  parser.add_argument('checked_off_by_id',
    type = int
    )
  parser.add_argument('instructor_id',
    type = int
    )

  def get(self, taskname):
    task = TaskModel.find_by_name(taskname)
    if task:
      return task.json()
    return {'message': 'Task not found'}, 404


  def post(self, taskname):
    if TaskModel.find_by_name(taskname):
      return {'message': "A task with that description already exists"}, 400

    data = Task.parser.parse_args()
    print(data)
    task = TaskModel(taskname, data['task_description'], data['completed'], data['completion_date'], data['checked_off_by_id'], data['instructor_id'])
    # task = TaskModel(taskname, **data)

    try:
      task.save_to_db()
    except:
      return{"message": "An error occurred inserting the task"}, 500

    return task.json(), 201
    

  def delete(self, taskname):
    task = TaskModel.find_by_name(taskname)
    if task:
      task.delete_from_db()

    return {"message": "Task deleted"}


  def put(self, taskname):
    data = Task.parser.parse_args()
    task = TaskModel.find_by_name(taskname)

   
    if task is None:
      task = TaskModel(taskname, data['task_description'], data['completed'], data['completion_date'], data['checked_off_by_id'], data['instructor_id'])
      
    else:
      # task = TaskModel(data['task_description'], data['completed'], data['completion_date'], data['checked_off_by_id'], data['instructor_id'])
      task.task_description = data['task_description']

    task.save_to_db()
    return task.json()


class Tasks(Resource):
  def get(self):
    return {'tasks': [task.json() for task in TaskModel.query.all()]}
  