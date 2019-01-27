# Libraries
import sqlite3
from db import db

# Classes
class UserModel(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String)
  job_title = db.Column(db.String)
  team = db.Column(db.String)

  def __init__(self, name, job_title, team):
    self.name = name
    self.job_title = job_title
    self.team = team


  def json(self):
    return {'id': self.id,
            'name': self.name,
            'job_title': self.job_title,
            'location': self.team}

  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id = _id).first()


  def save_to_db(self):
    db.session.add(self)
    db.session.commit()

  def delete_from_db(self):
    db.session.delete(self)
    db.session.commit()