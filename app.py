# import libraries

import os
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

# from flask_cors import CORS

# from flask_env import MetaFlaskEnv
from datetime import timedelta

from resources.task import Task, Tasks, UnallocatedTasks
from resources.sequence import Sequence, Sequences, TaskList, UserTask
from resources.position import Position, Positions
from resources.user import User, Users
from resources.template import Template, Templates
from resources.set import Set, Sets, AddSequence

from settings.config import DefaultConfig

# from settings.dev_config import DevConfig

# from config import DefaultConfig
print("<<<<< <<<< <<< << <! --- !> >> >>> >>>> >>>>>")
print("EnviromenT: " + os.environ.get("FLASK_ENV"))
# print(SQLALCHEMY_DATABASE_URI)
# environment = os.environ.get("FLASK_ENV")

environment = os.environ.get("FLASK_ENV")
app = Flask(__name__)
# CORS(app)


if environment == "development":
    # print("Development environment")
    # from settings.config import DevConfig
    from settings.dev_config import DevConfig

    app.config.from_object(DevConfig)

if environment == "test":
    # print("Test Environment")
    from settings.test_config import TestConfig

    app.config.from_object(TestConfig)


if environment == "production":
    # print("Production environment")
    from settings.prod_config import ProdConfig

    app.config.from_object(ProdConfig)


# from dotenv import load_dotenv
from resources.google_login import (
    GoogleLogin,
    GoogleAuthorize,
    GoogleLogout,
    GetCurrentUser,
)


# Configs & initialisations
# load_dotenv(".env")
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config.from_object(DefaultConfig)

app.permanent_session_lifetime = timedelta(minutes=5)

api = Api(app)
jwt = JWTManager(app)

# Endpoints
# region
api.add_resource(Users, "/api/users")
api.add_resource(User, "/api/user/<string:userid>")

api.add_resource(Tasks, "/api/tasks")
api.add_resource(Task, "/api/task")
api.add_resource(UnallocatedTasks, "/api/unallocatedtasks")

api.add_resource(Positions, "/api/positions")
api.add_resource(Position, "/api/position")

api.add_resource(Templates, "/api/templates")
api.add_resource(Template, "/api/template")

api.add_resource(Sets, "/api/sets")
api.add_resource(Set, "/api/set")
api.add_resource(AddSequence, "/api/addsequence/<int:set_id>")

api.add_resource(Sequences, "/api/sequences")
api.add_resource(Sequence, "/api/sequence/<int:_id>")
api.add_resource(TaskList, "/api/tasklist/<int:set_id>")
api.add_resource(UserTask, "/api/usertask")

api.add_resource(GoogleLogin, "/login/google")
api.add_resource(
    GoogleAuthorize,
    "https://onb0ardingapp.azurewebsites.net/login/google/authorized",
    endpoint="google.authorize",
)

api.add_resource(GetCurrentUser, "/api/getcurrentuser")
api.add_resource(GoogleLogout, "/api/logout")
# endregion

# region
# api.add_resource(Users, "https://onb0ardingapp.azurewebsites.net/api/users")
# api.add_resource(
#     User, "https://onb0ardingapp.azurewebsites.net/api/user/<string:userid>"
# )

# api.add_resource(Tasks, "https://onb0ardingapp.azurewebsites.net/api/tasks")
# api.add_resource(Task, "https://onb0ardingapp.azurewebsites.net/api/task")
# api.add_resource(
#     UnallocatedTasks, "https://onb0ardingapp.azurewebsites.net/api/unallocatedtasks"
# )

# api.add_resource(Positions, "https://onb0ardingapp.azurewebsites.net/api/positions")
# api.add_resource(Position, "https://onb0ardingapp.azurewebsites.net/api/position")

# api.add_resource(Templates, "https://onb0ardingapp.azurewebsites.net/api/templates")
# api.add_resource(Template, "https://onb0ardingapp.azurewebsites.net/api/template")

# api.add_resource(Sets, "https://onb0ardingapp.azurewebsites.net/api/sets")
# api.add_resource(Set, "https://onb0ardingapp.azurewebsites.net/api/set")
# api.add_resource(
#     AddSequence, "https://onb0ardingapp.azurewebsites.net/api/addsequence/<int:set_id>"
# )

# api.add_resource(Sequences, "https://onb0ardingapp.azurewebsites.net/api/sequences")
# api.add_resource(
#     Sequence, "https://onb0ardingapp.azurewebsites.net/api/sequence/<int:_id>"
# )
# api.add_resource(
#     TaskList, "https://onb0ardingapp.azurewebsites.net/api/tasklist/<int:set_id>"
# )
# api.add_resource(UserTask, "https://onb0ardingapp.azurewebsites.net/api/usertask")

# api.add_resource(GoogleLogin, "https://onb0ardingapp.azurewebsites.net/login/google")
# api.add_resource(
#     GoogleAuthorize,
#     "https://onb0ardingapp.azurewebsites.net/login/google/authorized",
#     endpoint="google.authorize",
# )

# api.add_resource(
#     GetCurrentUser, "https://onb0ardingapp.azurewebsites.net/api/getcurrentuser"
# )
# api.add_resource(GoogleLogout, "https://onb0ardingapp.azurewebsites.net/api/logout")
# endregion


from db import db

db.init_app(app)

# Main
if __name__ == "__main__":
    # from db import db

    # db.init_app(app)
    app.run(port=5000, debug=True)
