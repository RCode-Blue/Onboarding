# Libraries
import sqlite3
from db import db

# Classes
class UserModel(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key = True)
  google_id = db.Column(db.String)
  email = db.Column(db.String)
  given_name = db.Column(db.String)
  family_name = db.Column(db.String)
  picture = db.Column(db.String)
  hd = db.Column(db.String)
  token = db.Column(db.Text)
  created_at = db.Column(db.String)

  def __init__(self, email, given_name, family_name):
    self.email = email
    self.given_name = given_name
    self.family_name = family_name


  def json(self):
    return {
      'id': self.id,
      'google_id': self.google_id, 
      'email': self.email,
      'given_name': self.given_name,
      'family_name': self.family_name,
      'token': self.token,
      'created_at': self.created_at}


  @classmethod
  def find_by_email(cls, email):
    return cls.query.filter_by(email = email).first()

  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id = _id).first()


  def save_to_db(self):
    db.session.add(self)
    db.session.commit()

  def delete_from_db(self):
    db.session.delete(self)
    db.session.commit()