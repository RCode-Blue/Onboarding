from db import db


class LoginModel(db.Model):
    __tablename__ = "templates"

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer)

    def __init__(self, userid):
        self.userid = userid

    @classmethod
    def find_by_userid(cls, userid):
        return cls.query.filter_by(userid=userid).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

