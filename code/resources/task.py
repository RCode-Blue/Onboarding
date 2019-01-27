from flask_restful import Resource, reqparse
from models.task import TaskModel
from datetime import datetime

class Task(Resource):
  #region
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
  parser.add_argument('completion_date',
    type = str
    )
  parser.add_argument('checked_off_by',
    type = int
    )
  parser.add_argument('instructor_id',
    type = int
    )
  parser.add_argument('task_notes',
    type = str
    )
  #endregion


  # GET (taskname) ----------------
  #region
  # def get(self, taskname):
  #   task = TaskModel.find_by_name(taskname)
  #   if task:
  #     return task.json()
  #   return {'message': 'Task not found'}, 404
  #endregion

  # GET (_id) ----------------
  #region
  def get(self, _id):
    task = TaskModel.find_by_id(_id)
    if task:
      return task.json()
    return {'message': 'Task not found'}, 404
  #endregion

  # def get(self, taskDescription):
  #   task = TaskModel.find_by_description(taskDescription)
  #   if task:
  #     return task.json()
  #   return {'message': 'Task not found'}, 404




  # POST (taskname) ----------------
  #region
  def post(self, taskname):
    if TaskModel.find_by_name(taskname):
      return {"message": "A task with that description already exists"}, 400

    data = Task.parser.parse_args()
    # print(data)
    task = TaskModel(taskname, 
      data['task_description'], 
      data['completed'],
      data['completion_date'],
      data['checked_off_by'], 
      data['instructor_id'],
      data['task_notes']      
      )
    # task = TaskModel(taskname, **data)

    try:
      task.save_to_db()
    except:
      return { "message": "An error occurred inserting the task" }, 500

    return task.json(), 201
  #endregion    

  # POST (taskDescription) ----------------
  #region
  # def post(self, taskDescription):
  #   if TaskModel.find_by_description(taskDescription):
  #     return {'message': "A task with that description already exists"}, 400

  #   data = Task.parser.parse_args()
  #   print(data)
  #   task = TaskModel(data['task_name'], 
  #     taskDescription, 
  #     data["completed"], 
  #     data['completion_date'], 
  #     data['checked_off_by'], 
  #     data['instructor_id'],
  #     data['task_notes'])

  #   try:
  #     task.save_to_db()
  #   except:
  #     return{"message": "An error occurred inserting the task"}, 500

  #   return task.json(), 201
  #endregion    




  # DELETE (taskname) ----------------
  #region
  def delete(self, taskname):
    task = TaskModel.find_by_name(taskname)
    if task:
      task.delete_from_db()

    return {"message": "Task deleted"}
  #endregion

  #DELETE (taskDescription) ----------------
  #region
  # def delete(self, taskDescription):
  #   task = TaskModel.find_by_description(taskDescription)
  #   if task:
  #     task.delete_from_db()

  #   return {"message": "Task deleted"}
  #endregion

  #DELETE (taskId) ----------------
  #region
  def delete(self, taskId):
    task = TaskModel.find_by_id(taskId)
    if task:
      task.delete_from_db()

    return {"message": "Task deleted"}
  #endregion




  # PUT (taskname) ----------------
  #region
  def put(self, taskname):
    data = Task.parser.parse_args()
    task = TaskModel.find_by_name(taskname)

   
    if task is None:
      task = TaskModel(taskname,
        data['completed'], 
        data['completion_date'], 
        data['checked_off_by'], 
        data['task_notes'])
      
    else:
      task.task_description = data['task_description']

    task.save_to_db()
    return task.json()
    #endregion





class Tasks(Resource):
  def get(self):
    return {"tasks": [task.json() for task in TaskModel.query.all()]}
  