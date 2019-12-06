import os
from flask import g
from flask_oauthlib.client import OAuth

oauth = OAuth()


# Google Login
google = oauth.remote_app(
    "google",
    consumer_key="xxxxxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.apps.googleusercontent.com",
    consumer_secret="xxxxxxxxxxxxxxxxxxxxxxxx",
    request_token_params={"scope": ["profile", "email"]},
    base_url="https://www.googleapis.com/oauth2/v1/",
    request_token_url=None,
    access_token_method="POST",
    access_token_url="https://accounts.google.com/o/oauth2/token",
    authorize_url="https://accounts.google.com/o/oauth2/auth",
)


@google.tokengetter
def get_google_token():
    if "access_token" in g:
        return g.access_token


class DevConfig:
    POSTGRES = {
        "user": "xxxxx",
        "pw": "xxxxxx",
        "db": "xxxxx",
        "host": "localhost",
        "port": "5432",
    }

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s" % POSTGRES
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPOGATE_EXCEPTIONS = True
