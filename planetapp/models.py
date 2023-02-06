from flask_login import UserMixin

from .extensions import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    bio = db.Column(db.String)
    settings = db.relationship("Settings", uselist=False, back_populates="user")


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    title = db.Column(db.String(20), nullable=False, unique=True)
    image_url = db.Column(db.String(255), nullable=False)
    desc = db.Column(db.String, nullable=False)


class Settings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    zoom = db.Column(db.Integer, nullable=False)
    speed = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", back_populates="settings")
