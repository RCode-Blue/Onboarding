# Libraries
import sqlite3
from db import db

# Classes
class PositionModel(db.Model):
  __tablename__ = 'positions'

  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  template_id = db.Column(db.Integer, db.ForeignKey('templates.id'))
  task_id = db.Column(db.Integer, db.ForeignKey('tasks.id')) #use table name
  position_no = db.Column(db.Integer)

  task = db.relationship('TaskModel')
  
  template = db.relationship('TemplateModel')
  # template = db.relationship('TemplateModel', back_populates = 'positions') #use ref name

  def __init__(self, template_id, task_id, position_no):
    self.template_id = template_id
    self.task_id = task_id
    self.position_no = position_no


  def json(self):
    return {'position_id': self.id,
            'template_id': self.template_id,
            'task_id': self.task_id,
            'position_no': self.position_no
            }


  def json_task(self):
    # print(self.template.template_name)
    return {'position_id': self.id,
            'template_id': self.template_id,
            'template_name': self.template.template_name,
            'template_description': self.template.description,
            'task_id': self.task_id,
            'position_no': self.position_no,
            # 'tasks': [task.json() for task in self.tasks.all()]}
            'instructor_id': self.task.instructor_id,
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
  def find_by_sequence(cls, sequenceid):
    return cls.query.filter_by(sequence_id = sequenceid)

  @classmethod
  def find_by_template(cls, templateid):
    return cls.query.filter_by(template_id = templateid)

  @classmethod
  def find_by_position(cls, templateid, taskid, positionno):
    return cls.query.filter_by(
      template_id = templateid, 
      task_id = taskid, 
      position_no = positionno).first()


  def save_to_db(self):
    db.session.add(self)
    db.session.commit()


  def delete_from_db(self):
    db.session.delete(self)
    db.session.commit()

