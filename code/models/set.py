# Libraries
import sqlite3
from db import db

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

  template = db.relationship('TemplateModel')

  def __init__(self, 
                template_id, 
                description,
                city,
                start_date,
                employee_id,
                manager_id,
                buddy_id):
    self.template_id = template_id
    self.description = description
    self.city = city
    self.start_date = start_date
    self.employee_id = employee_id
    self.manager_id = manager_id
    self.buddy_id = buddy_id

  
  def json(self):
    return {'set_id': self.id,
            'template_id': self.template_id,
            'description': self.description,
            'city': self.city,
            'start_date': self.start_date,
            'employee_id': self.employee_id,
            'manager_id': self.manager_id,
            'buddy_id': self.buddy_id
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
            'template': [self.template.json_positions()]
            }


  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id = _id).first()