import os
from flask import g
from flask_oauthlib.client import OAuth

google_auth_consumer_key = os.environ.get("GOOGLE_AUTH_CONSUMER_KEY")
google_auth_consumer_secret = os.environ.get("GOOGLE_AUTH_CONSUMER_SECRET")

db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_database = os.environ.get("DB_DATABASE")
db_host = os.environ.get("DB_HOST")
db_port = os.environ.get("DB_PORT")
db_uri = os.environ.get("DATABASE_URL")


oauth = OAuth()


# Google Login
google = oauth.remote_app(
    "google",
    consumer_key=google_auth_consumer_key,
    consumer_secret=google_auth_consumer_secret,
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


class ProdConfig:
    POSTGRES = {
        "user": db_user,
        "pw": db_password,
        "db": db_database,
        "host": db_host,
        "port": db_port,
    }

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = db_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPOGATE_EXCEPTIONS = True

