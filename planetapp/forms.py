from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, TextAreaField, DateField
from wtforms.validators import InputRequired, Length, ValidationError
from .models import User


class UserForm(FlaskForm):
    username = StringField(validators=[
        InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    email = EmailField(validators=[
        InputRequired(), Length(min=4, max=30)], render_kw={"placeholder": "Email"})

    birth_date = DateField(validators=[
        InputRequired()], render_kw={"placeholder": "Birth date"})

    bio = TextAreaField(render_kw={"placeholder": "Bio"})


class RegisterForm(UserForm):
    password = PasswordField(validators=[
        InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError('That username already exists. Please choose a different one.')

    def validate_email(self, email):
        existing_user_email = User.query.filter_by(
            email=email.data).first()
        if existing_user_email:
            raise ValidationError('That email already exists. Please choose a different one.')


class EditProfileForm(UserForm):
    submit = SubmitField('Submit changes')

    def validate_username(self, username):
        existing_user = User.query.filter_by(
            username=username.data).first()
        if existing_user and existing_user.username != current_user.username:
            raise ValidationError('That username already exists. Please choose a different one.')

    def validate_email(self, email):
        existing_user = User.query.filter_by(
            email=email.data).first()
        if existing_user and existing_user.email != current_user.email:
            raise ValidationError('That email already exists. Please choose a different one.')


class LoginForm(FlaskForm):
    username = StringField(validators=[
        InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
        InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')
