# Libraries
import sqlite3
from db import db

# Classes
class PositionModel(db.Model):
  __tablename__ = 'positions'

  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  template_id = db.Column(db.Integer)
  task_id = db.Column(db.Integer, db.ForeignKey('tasks.id')) #use table name
  position_no = db.Column(db.Integer)

  task = db.relationship('TaskModel')
  # sequence = db.relationship('SequenceModel', backref='pos')

  def __init__(self, template_id, task_id, position_no):
    self.template_id = template_id
    self.task_id = task_id
    self.position_no = position_no


  def json(self):
    return {'id': self.id,
            'template_id': self.template_id,
            'task_id': self.task_id,
            'position_no': self.position_no
            }


  def json_task(self):
    return {'id': self.id,
            'template_id': self.template_id,
            'task_id': self.task_id,
            'position_no': self.position_no,
            # 'tasks': [task.json() for task in self.tasks.all()]}
            'task_description': self.task.task_description,
            'completion_date': self.task.completion_date,
            'completed': self.task.completed,
            'checked_off_by': self.task.checked_off_by,
            'task_notes': self.task.task_notes
            }


  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id = _id).first()

  @classmethod
  def find_by_name(cls, positionname):
    return cls.query.filter_by(position_name = positionname).first()

  @classmethod
  def find_by_sequence(cls, sequenceid):
    return cls.query.filter_by(sequence_id = sequenceid)

  @classmethod
  def find_by_template(cls, templateid):
    return cls.query.filter_by(template_id = templateid)


  def save_to_db(self):
    db.session.add(self)
    db.session.commit()


  def delete_from_db(self):
    db.session.delete(self)
    db.session.commit()

