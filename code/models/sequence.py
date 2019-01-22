import sqlite3
from db import db


# Classes
class SequenceModel(db.Model):
  __tablename__ = 'sequences'

  id = db.Column(db.Integer, primary_key = True)
  set_id = db.Column(db.Integer, db.ForeignKey('sets.id'))
  task_description = db.Column(db.Text)
  completed = db.Column(db.Boolean)
  completion_date = db.Column(db.Text)
  checked_off_by = db.Column(db.Integer, db.ForeignKey('users.id'))
  instructor_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  task_notes = db.Column(db.Text)

  _set = db.relationship('SetModel', back_populates = 'sequence')


  def __init__(self, 
              set_id,
              task_description,
              completed,
              completion_date,
              checked_off_by,
              instructor_id,
              task_notes):
    self.set_id = set_id
    self.task_description = task_description
    self.completed = completed
    self.completion_date = completion_date
    self.checked_off_by = checked_off_by
    self.instructor_id = instructor_id
    self.task_notes = task_notes


  def json(self):
    return {'id': self.id,
            'set_id': self.set_id,
            'task_description': self.task_description,
            'completed': self.completed,
            'completion_date': self.completion_date,
            'instructor_id': self.instructor_id,
            'task_notes': self.task_notes
            }


  def json_positions(self):
    return {'id': self.id,
            'set_id': self.set_id,
            'task_description': self.task_description,
            'completed': self.completed,
            'completion_date': self.completion_date,
            'instructor_id': self.instructor_id,
            'task_notes': self.task_notes,
            'set': [self._set.json_template()]
            # 'set': [self._set.json()]
            }



  # def populate(self):
  #   self.task_description = self.set.description

  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id = _id).first()

  
  def save_to_db(self):
    db.session.add(self)
    db.session.commit()


  def delete_from_db(self):
    db.session.delete(self)
    db.session.commit()
