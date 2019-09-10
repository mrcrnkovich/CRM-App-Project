# app/auth/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from app.models import User

class RegistrationForm(FlaskForm):

	#Form for users to create new account

	username =StringField('Username', validators=[DataRequired()])
	email = StringField('Email Address', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators = [DataRequired(), EqualTo('confirm_password')])
	confirm_password = PasswordField('Confirm Password')
	submit = SubmitField('Register')

class LoginForm(FlaskForm):

	#Log users in

	email = StringField('Email Address', validators = [DataRequired(), Email()])
	password = StringField('Password', validators = [DataRequired()])
	submit = SubmitField('Login')