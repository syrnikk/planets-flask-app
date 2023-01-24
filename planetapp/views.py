from flask import Blueprint, render_template
from flask_login import current_user

from planetapp import db
from planetapp.models import Planet, Settings

views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template('index.html')


@views.route('/wiki/', defaults={'planet_name': 'sun'})
@views.route('/wiki/<planet_name>')
def wiki(planet_name):
    planet = db.session.query(Planet).filter_by(name=planet_name).one()
    return render_template('wiki.html', planet=planet)


@views.route('/animation')
def animation():
    settings = db.session.query(Settings).filter_by(user_id=current_user.id).first() if current_user.is_authenticated else None
    return render_template('animation.html', settings=settings)
