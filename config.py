import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'secretkey'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
