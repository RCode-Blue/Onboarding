from flask_restful import Resource, reqparse
from models.sequence import SequenceModel
from models.set import SetModel
import datetime

from db import db


class Sequence(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('set_id',
                        type=int)
    parser.add_argument('task_description',
                        type=str)
    parser.add_argument('task_position',
                        type=int)
    parser.add_argument('completed',
                        type=bool)
    parser.add_argument('completion_date',
                        type=str)
    parser.add_argument('checked_off_by',
                        type=int)
    parser.add_argument('instructor_id',
                        type=int)
    parser.add_argument('task_notes',
                        type=str)

    # GET
    def get(self, _id):
        sequence = SequenceModel.find_by_id(_id)
        if sequence:
            # return sequence.json()
            return sequence.json_positions()
        return {'message': 'Task not found'}, 404

    # PUT (modify)
    def put(self):
        data = Sequence.parser.parse_args()
        sequence = SequenceModel.find_by_task_description(
            data['task_description'])

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
        return {sequence: sequence.json()}

    # DELETE
    def delete(self, _id):
        sequence = SequenceModel.find_by_name(_id)
        if sequence:
            sequence.delete_from_db()

        return{"message": "Sequence deleted"}


class Sequences(Resource):
    def get(self):
        return {"sequences": [sequence.json() for sequence in SequenceModel.query.all()]}


class TaskList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("set_id", type=int)

    def get(self, set_id):
        _set = SetModel.find_by_id(set_id)
        tasks = SequenceModel.find_by_set_id(set_id)

        if tasks:
            user_tasks = []
            for task in tasks:
                user_tasks.append(task.json())
            sorted_user_tasks = sorted(
                user_tasks, key=lambda x: x["task_position"])
            return {
                "set": _set.json(),
                # 'tasks': [task.json() for task in tasks]}
                "tasks": sorted_user_tasks}

        else:
            return {"message": "No task found"}


class UserTask(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("user_task_id", type=int)  # id
    parser.add_argument("set_id", type=int)
    parser.add_argument("task_description", type=str)
    parser.add_argument("task_position", type=int)
    parser.add_argument("completed", type=bool)
    # parser.add_argument("completion_date", type=str)
    parser.add_argument("completion_date_year", type=int)
    parser.add_argument("completion_date_month", type=int)
    parser.add_argument("completion_date_date", type=int)
    parser.add_argument("checked_off_by", type=int)
    parser.add_argument("instructor_id", type=str)
    parser.add_argument("task_notes", type=str)

    # GET
    def get(self):
        data = UserTask.parser.parse_args()
        usertask = SequenceModel.find_by_id(data['user_task_id'])

        if usertask:
            return {
                "user_task": usertask.json()
            }
        else:
            return {"message": "User task not found"}

    # PUT (modify)
    def put(self):
        data = UserTask.parser.parse_args()
        user_task = SequenceModel.find_by_id(data["user_task_id"])

        # print(data)

        if user_task:
            if data["completed"] == True:
                formatted_completion_date = datetime.date(
                    data["completion_date_year"], data["completion_date_month"], data["completion_date_date"])

            # elif data["completed"] == False:
            else:
                formatted_completion_date = None

            user_task.completed = data["completed"]
            user_task.completion_date = formatted_completion_date
            try:
                user_task.save_to_db()

                new_user_task = SequenceModel.find_by_id(data["user_task_id"])
                return {
                    "current_set_task": new_user_task.json()
                }
            except:
                return {"message": "An error occured saving the task"}
        else:
            return {"message": "Task not found"}
