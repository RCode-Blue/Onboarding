from flask_restful import Resource, reqparse
from datetime import datetime
from models.user import UserModel


class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str)
    parser.add_argument("job_title", type=str)
    parser.add_argument("team", type=str)

    # GET
    def get(self, userid):
        user = UserModel.find_by_id(userid)
        if user:
            return user.json()
        return {"message": "User not found"}, 404

    # PUT
    def put(self):
        pass

    # POST

    # DELETE
    def delete(self, userid):
        user = UserModel.find_by_id(userid)
        if not user:
            return {"message": "user not found"}, 404

        user.delete_from_db()
        return {"message": "user deleted"}, 200


# USERS
class Users(Resource):
    def get(self):
        return {"users": [user.json() for user in UserModel.query.all()]}

