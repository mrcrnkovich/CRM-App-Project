# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from app.models import User


class LoginForm(FlaskForm):

    # Log users in

    email = StringField('Email Address',
                validators=[DataRequired(), Email()])
    password = StringField('Password',
            validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    pass
