import time
import os

from flask import g, request, url_for, jsonify, session, redirect
from flask_restful import Resource
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
)

from models.user import UserModel


environment = os.environ.get("FLASK_ENV")
# print("----- google_login environment: " + environment + "-----")
# from oa import google


if environment == "development":
    # print("Development environment")
    from settings.dev_config import google

if environment == "test":
    # print("Development environment")
    from settings.test_config import google

if environment == "production":
    # from settings.config import DefaultConfig
    # print("Production environment")
    from settings.prod_config import google


class GoogleLogin(Resource):
    @classmethod
    def get(cls):
        # return google.authorize(url_for("google.authorize", _external=True))
        return google.authorize(
            "https://onb0ardingapp.azurewebsites.net/login/google/authorized"
        )


class GoogleAuthorize(Resource):
    @classmethod
    def get(cls):
        print("------googleAUthorize-----")
        resp = google.authorized_response()
        if resp is None or resp.get("access_token") is None:
            error_response = {
                "error": request.args["error"],
                "error_description": request.args["error_description"],
            }
            return error_response

        g.access_token = resp["access_token"]
        google_user = google.get("userinfo")
        google_email = google_user.data["email"]
        # google_id = google.user.data['id']
        # print(google_user)

        # region
        # user = UserModel.find_by_email(google_email)
        # if not user:
        #   newUser = UserModel(
        #     google_email,
        #     google_user.data['given_name'],
        #     google_user.data['family_name']
        #   )
        #   newUser.save_to_db()
        # endregion

        user = UserModel.find_by_email(google_email)
        if not user:
            newUser = UserModel(
                google_email,
                google_user.data["given_name"],
                google_user.data["family_name"],
            )
            newUser.save_to_db()
            time.sleep(5.5)
            # TODO: implement "try again" code for the above, perhaps using Tenacity

        access_token = create_access_token(identity=user.id, fresh=True)
        refresh_token = create_refresh_token(user.id)

        session["user_id"] = user.id
        session.permanent = True

        # return {
        #   # "access_token": access_token,
        #   # "refresh_token": refresh_token,
        #   "user_id": user.id,
        #   # "google_username": google_user.data['email'],
        #   "google_userid": google_user.data['id']
        #   }, 200

        return redirect(
            # "http://localhost:3000/dashboard"
            "http://localhost:3000/"
            # "https://onb0ardingapp.azurewebsites.net"
        )


class GoogleLogout(Resource):
    @classmethod
    def get(cls):
        session.pop("user_id", None)
        session.modified = True
        return redirect("http://localhost:3000")
        # return redirect("https://onb0ardingapp.azurewebsites.net")


class GetCurrentUser(Resource):
    @classmethod
    def get(cls):
        print(session)
        if "user_id" in session:
            if session["user_id"]:
                return {"user_id": session["user_id"]}
        return ""
