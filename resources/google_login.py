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
        print(("<- -- --- GoogleLogin --- -- ->"))
        return google.authorize(url_for("google.authorize", _external=True))


class GoogleAuthorize(Resource):
    @classmethod
    def get(cls):
        print("------googleAUthorize-----")
        resp = google.authorized_response()
        print(resp)
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
        # print(google_user.data)

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

        # region - DB
        # user_login = LoginModel.find_by_userid(user.id)
        # new_userlogin = LoginModel(
        #     user.id
        # )
        # new_userlogin.save_to_db()
        # time.sleep(5.5)
        # endregion

        session["user_id"] = user.id
        session.permanent = True
        print("---Google Authorize Session:")
        print(session)

        return redirect("http://localhost:3000/")
        # return redirect("https://lit-harbor-79520.herokuapp.com/")


class GoogleLogout(Resource):
    @classmethod
    def get(cls):
        print("<< -- --- GoogleLogout --- -- >>")
        session.pop("user_id", None)
        session.modified = True
        # session.permanent = True

        return redirect("http://localhost:3000")
        # return redirect("https://lit-harbor-79520.herokuapp.com/")


class GetCurrentUser(Resource):
    @classmethod
    def get(cls):
        print("|--- GetCurrentUser ---")
        print("GetCurrentUser Session:")
        print(session)

        if "user_id" in session:
            if session["user_id"]:
                return {"user_id": session["user_id"]}
        return ""


# region Client-Side


class GoogleLoginFE(Resource):
    @classmethod
    def get(cls):
        print(("<- -- --- GoogleLoginFE --- -- ->"))
        return google.authorize(url_for("google.authorizefe", _external=True))


class GoogleAuthorizeFE(Resource):
    @classmethod
    def get(cls):
        print("------googleAuthoriSeFE-----")
        resp = google.authorized_response()
        print(resp)
        if resp is None or resp.get("access_token") is None:
            error_response = {
                "error": request.args["error"],
                "error_description": request.args["error_description"],
            }
            return error_response

        g.access_token = resp["access_token"]
        google_user = google.get("userinfo")
        google_email = google_user.data["email"]

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

        # access_token = create_access_token(identity=user.id, fresh=True)
        # refresh_token = create_refresh_token(user.id)

        # session["user_id"] = user.id
        # session.permanent = True
        # print("Google Authorize Session:")
        # print(session)

        return {"user_id": user.id}

        return redirect("http://localhost:3000/")
        # return redirect("https://lit-harbor-79520.herokuapp.com/")


# endregion
