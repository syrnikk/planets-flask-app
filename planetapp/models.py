from flask_login import UserMixin
from .extensions import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    bio = db.Column(db.String)