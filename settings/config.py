import os

# if os.environ["FLASK_ENV"] == "dev":
#     from .dev_config import *
# if os.environ["FLASK_ENV"] == "prod":
#     from .prod_config import *


class DefaultConfig:
    SECRET_KEY = os.urandom(24)

    JWT_SECRET_KEY = os.urandom(36)
    JWT_TOKEN_LOCATION = "cookies"
    JWT_ACCESS_COOKIE_PATH = "/api/"
    JWT_REFRESH_COOKIE_PATH = "/TOKEN/REFRESH"
    JWT_COOKIE_CSRF_PROTECT = False

