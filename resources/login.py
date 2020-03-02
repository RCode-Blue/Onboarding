from flask import request
from flask_restful import Resource, reqparse
from models.login import LoginModel

class Login(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument("userid", type=int)

  # GET (userid)
  def get(self):
    data = Login.parser.parse_args()
    login = LoginModel.find_by_userid(data["userid"])
    if login:
      return {"user_id": login.userid}
    return ""

  # POST 
  def post(self):
    data = Login.parser.parse_args()

    login = LoginModel.find_by_userid(data["userid"])
    if login:
      return {"error": "The task already exists"}, 500
    else:
      newLogin = LoginModel(
        data["userid"]
      )
    try:
      newLogin.save_to_db