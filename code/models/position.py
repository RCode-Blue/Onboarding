# Libraries
import sqlite3
from db import db

# Classes
class PositionModel(db.Model):
  __tablename__ = 'position'

  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  position_name = db.Column(db.String)

  task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))
  sequence_id = db.Column(db.Integer)
  sequence_no = db.Column(db.Integer)

  tasks = db.relationship('TaskModel')
  

  def __init__(self, position_name, task_id, sequence_id, sequence_no):
    self.position_name = position_name
    self.task_id = task_id
    self.sequence_id = sequence_id
    self.sequence_no = sequence_no

  
  def json(self):
    return {'id': self.id,
            'position_name': self.position_name,
            'task_id': self.task_id,
            'sequence_id': self.sequence_id,
            'sequence_no': self.sequence_no
            }


  def json_task(self):
    # print(self.tasks.all())
    return {'id': self.id,
            'position_name': self.position_name,
            'task_id': self.task_id,
            'sequence_id': self.sequence_id,
            'sequence_no': self.sequence_no,
            'tasks': [task.json() for task in self.tasks.all()]}
            # 'tasks': [task.json() for task in self.tasks.first()]}


  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id = _id).first()

  @classmethod
  def find_by_name(cls, positionname):
    return cls.query.filter_by(position_name = positionname).first()


  @classmethod
  def find_by_sequence(cls, sequenceid):
    return cls.query.filter_by(sequence_id = sequenceid)


  def save_to_db(self):
    db.session.add(self)
    db.session.commit()


  def delete_from_db(self):
    db.session.delete(self)
    db.session.commit()

