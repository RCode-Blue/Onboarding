import sqlite3
from db import db

# Classes
class TemplateModel(db.Model):
  __tablename__ = 'templates'

  id = db.Column(db.Integer, primary_key = True)
  sequence_id = db.Column(db.String, db.ForeignKey('sequences.id'))

  description = db.Column(db.String)
  city = db.Column(db.String)
  start_date = db.Column(db.String)
  employee_id = db.Column(db.Integer)
  manager_id = db.Column(db.Integer)
  buddy_id = db.Column(db.Integer)

  sequences = db.relationship('SequenceModel')

  def __init__(self, sequence_id, description, city, start_date, employee_id, manager_id, buddy_id):
    self.sequence_id = sequence_id
    self.description = description
    self.city = city
    self.start_date = start_date
    self.employee_id = employee_id
    self.manager_id = manager_id
    self.buddy_id = buddy_id

  # JSON
  def json(self):
    return{'id': self.id,
           'sequence_id': self.sequence_id, 
           'description': self.description,
           'city': self.city,
           'start_date': self.start_date,
           'employee_id': self.employee_id,
           'manager_id': self.manager_id,
           'buddy_id': self.buddy_id
           }

  
  def json_sequence(self):
    print('-----------------------------')
    print(self.sequences.positions)
    print('-----------------------------')

    return {
      'description': self.description,
      'sequence_name': self.sequences.sequence_name
      # 'positions': [sequence.position.json_tasks() for sequence.position in self.sequence.positions]
    }


  # Methods
  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id = _id).first()


  def save_to_db(self):
    db.session.add(self)
    db.session.commit()

  def delete_from_db(self):
    db.session.delete(self)
    db.session.commit()