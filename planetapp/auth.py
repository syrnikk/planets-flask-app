from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, logout_user, login_user, current_user
from .extensions import db, bcrypt, login_manager
from .forms import LoginForm, RegisterForm, EditProfileForm
from .models import User

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('views.index'))
            else:
                flash('Incorrect password')
        else:
            flash('User does not exist')
    return render_template('login.html', form=form)


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data)
            new_user = User(username=form.username.data, password=hashed_password, email=form.email.data, birth_date=form.birth_date.data, bio=form.bio.data)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            flash('Username or email is not available')

    return render_template('register.html', form=form)


@auth.route('/profile')
def profile():
    return render_template('profile.html')


@auth.route('/edit-profile', methods=['GET', 'POST'])
def edit_profile():
    form = EditProfileForm(obj=current_user)

    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(current_user)
            db.session.commit()
            return redirect(url_for('auth.profile'))
        else:
            flash('Username or email is not available')

    return render_template('edit-profile.html', form=form)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
