from flask_restful import Resource, reqparse
from models.user import UserModel
from datetime import datetime

class User(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('name',
    type = str
    )
  parser.add_argument('job_title',
    type = str
    )
  parser.add_argument('team',
    type = str
    )

  # GET user
  def get(self, userid):
    user = UserModel.find_by_id(userid)
    if user:
      return user.json()
    return{'message': 'User not found'}, 404


  # POST user


  # DELETE user



  # PUT user


# USERS
class Users(Resource):
  def get(self):
    return {'users': [user.json() for user in UserModel.query.all()]}