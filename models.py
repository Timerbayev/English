from app import db
from datetime import date
import uuid
from flask_login import UserMixin


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"<role {self.name}>"


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    uuids = db.Column(db.String(40), unique=True, index=True, nullable=False,
                      default=str(uuid.uuid1()))
    name = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(20), nullable=True)
    data = db.Column(db.DATE, default=date.today())
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    def __repr__(self):
        return f"<user {self.name}>"


class Dictionary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eng = db.Column(db.String(100), nullable=False, unique=True)
    rus = db.Column(db.String(100), nullable=False, unique=True)
    story = db.Column(db.Text, nullable=False, unique=True)
    datas = db.Column(db.DATE, default=date.today(), nullable=True)

    def __repr__(self):
        return f"<id  {self.id}>"


class Profiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer)
    mobile = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"<profiles {self.id}>"


