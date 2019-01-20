# Libraries
import sqlite3
from db import db
import datetime

# Classes
class TaskModel(db.Model):
  __tablename__ = 'tasks'

  id = db.Column(db.Integer, primary_key = True)
  task_name = db.Column(db.String)
  task_description = db.Column(db.Text)
  completed = db.Column(db.Boolean)
  completion_date = db.Column(db.Text)
  checked_off_by = db.Column(db.Integer)
  instructor_id = db.Column(db.Integer)
  task_notes = db.Column(db.Text)

  # position = db.relationship('PositionModel')


  def __init__(self, 
    task_name, 
    task_description, 
    completed, 
    completion_date, 
    checked_off_by, 
    instructor_id, 
    task_notes):
      self.task_name = task_name
      self.task_description = task_description
      self.completed = completed
      self.completion_date = completion_date
      self.checked_off_by = checked_off_by
      self.instructor_id = instructor_id
      self.task_notes = task_notes

  def json(self):
    return {'id': self.id,
            'task_name': self.task_name,
            'description': self.task_description,
            'completed': self.completed,
            'completion_date': self.completion_date,
            'checked_off_by': self.checked_off_by,
            'instructor_id': self.instructor_id,
            'task_notes': self.task_notes}




  @classmethod
  def find_by_description(cls, description):
    return cls.query.filter_by(task_description = description).first()

  @classmethod
  def find_by_name(cls, name):
    return cls.query.filter_by(task_name = name).first()

  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id = _id).first()

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()

  def delete_from_db(self):
    db.session.delete(self)
    db.session.commit()