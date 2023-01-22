from flask import Flask

from .auth import auth
from .extensions import bcrypt, db, login_manager
from .views import views
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    app.register_blueprint(views)
    app.register_blueprint(auth)

    with app.app_context():
        db.create_all()

    return app
