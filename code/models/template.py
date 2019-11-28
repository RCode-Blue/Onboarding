import sqlite3
from db import db

# Classes


class TemplateModel(db.Model):
    __tablename__ = 'templates'

    id = db.Column(db.Integer, primary_key=True)
    # position_id = db.Column(db.String, db.ForeignKey('sequences.id'))

    template_name = db.Column(db.String)
    description = db.Column(db.String)

    positions = db.relationship('PositionModel', back_populates='template')

    # _set = db.relationship('SetModel')

    # sequences = db.relationship('SequenceModel')

    def __init__(self, template_name, description):
        self.template_name = template_name
        self.description = description

    # JSON

    def json(self):
        return{'id': self.id,
               'template_name': self.template_name,
               'description': self.description,
               'template_id': self.id
               }

    def json_positions(self):
        return {
            'template_name': self.template_name,
            'description': self.description,
            'template_id': self.id,
            'positions': [position.json_task() for position in self.positions]
            # 'positions': [position.json() for position in self.positions]
        }

    # Methods
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_template_name(cls, template_name):
        return cls.query.filter_by(template_name=template_name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        for position in self.positions:
            position.delete_from_db()
        db.session.delete(self)
        db.session.commit()
