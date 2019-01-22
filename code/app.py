# import libraries
from flask import Flask
from flask_restful import Api

from resources.task import Task, Tasks
from resources.sequence import Sequence, Sequences
from resources.position import Position, Positions
from resources.user import User
from resources.template import Template, Templates
from resources.set import Set, Sets

# Configs & initialisations
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)


# Endpoints
api.add_resource(Tasks, '/tasks')
# api.add_resource(Task,  '/task/<string:taskname>')
api.add_resource(Task,  '/task/<string:taskname>')

api.add_resource(Sequences, '/sequences')
api.add_resource(Sequence,  '/sequence/<int:_id>')

api.add_resource(Positions, '/positions')
api.add_resource(Position,  '/position/<int:_id>')

api.add_resource(User, '/user/<string:userid>')

api.add_resource(Templates, '/templates')
api.add_resource(Template, '/template/<int:templateid>')

api.add_resource(Sets, '/sets')
api.add_resource(Set, '/set/<int:_id>')

# Main
if __name__ == '__main__':
  from db import db
  db.init_app(app)
  app.run(port = 5000, debug = True)

