# Libraries
import sqlite3
from db import db
from models.sequence import SequenceModel
from models.user import UserModel

# Classes
class SetModel(db.Model):
  __tablename__ = 'sets'

  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  template_id = db.Column(db.Integer, db.ForeignKey('templates.id'))
  description = db.Column(db.Text)
  city = db.Column(db.Text)
  start_date = db.Column(db.Text)
  employee_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  manager_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  buddy_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  sequence_id = db.Column(db.Integer, db.ForeignKey('sequences.id'))

  template = db.relationship('TemplateModel')

  # sequence = db.relationship('SequenceModel')
  sequence = db.relationship('SequenceModel', foreign_keys=[sequence_id], uselist = False, lazy='noload')
  # sequence = db.relationship('SequenceModel', foreign_keys=[sequence_id], uselist = False)
  # sequence = db.relationship('SequenceModel', uselist = False)

  employee = db.relationship('UserModel', foreign_keys=[employee_id])
  manager = db.relationship('UserModel', foreign_keys = [manager_id])
  buddy = db.relationship('UserModel', foreign_keys = [buddy_id])


  def __init__(self, 
                template_id, 
                description,
                city,
                start_date,
                employee_id,
                manager_id,
                buddy_id,
                sequence_id):
    self.template_id = template_id
    self.description = description
    self.city = city
    self.start_date = start_date
    self.employee_id = employee_id
    self.manager_id = manager_id
    self.buddy_id = buddy_id
    self.sequence_id = sequence_id


  
  def json(self):
    return {'set_id': self.id,
            'template_id': self.template_id,
            'description': self.description,
            'city': self.city,
            'start_date': self.start_date,
            'employee_id': self.employee_id,
            'manager_id': self.manager_id,
            'buddy_id': self.buddy_id,
            'sequence_id': self.sequence_id
            }

  
  def json_template(self):
    return {'set_id': self.id,
            'template_id': self.template_id,
            'description': self.description,
            'city': self.city,
            'start_date': self.start_date,
            'employee_id': self.employee_id,
            'manager_id': self.manager_id,
            'buddy_id': self.buddy_id,
            'sequence_id': self.sequence_id,
            'template': [self.template.json_positions()],
            # 'sequence': [self.sequence.json()],
            # 'sequence_id': self.sequence.id,
            'employee': [self.employee.json()],
            'manager': [self.manager.json()],
            'buddy': [self.buddy.json()]
            }


  # data to be used to create sequence entries
  def json_sequence(self):
    return {'set_id': self.id,
            'template_id': self.template_id,
            'description': self.description,
            'city': self.city,
            'start_date': self.start_date,
            'employee_id': self.employee_id,
            'manager_id': self.manager_id,
            'buddy_id': self.buddy_id,
            'sequence_id': self.sequence_id,
            'template': [self.template.json_positions()],
            # 'sequence': [self.sequence.json()],
            # 'sequence_id': self.sequence.id,
            'employee': [self.employee.json()],
            'manager': [self.manager.json()],
            'buddy': [self.buddy.json()]
            }


  @classmethod
  def create_new_sequence(cls, _id, set, data):
    set.sequence_id = data['sequence_id']
    
    for position in set.template.positions:
      newSeq =  SequenceModel(_id, 
        position.task.task_description, 
        position.position_no, 
        position.task.completed, 
        position.task.completion_date,  
        position.task.checked_off_by, 
        position.task.instructor_id, 
        position.task.task_notes)
      try:
        newSeq.save_to_db()
      except:
        return {"message": "An error occured inserting this sequence"}, 500
        
     # return sequence.json(), 201



  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id = _id).first()

  @classmethod
  def find_by_sequence_id(cls, _id):
    return cls.query.filter_by(sequence_id = _id).first()