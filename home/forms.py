# app/auth/forms.py

from flask_wtf import FlaskForm
from wtforms import  StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo


class SearchForm(FlaskForm):

    # Log users in

    email = StringField('Email Address',
                validators=[DataRequired(), Email()])
    client_name = StringField('Client Name')
    submit = SubmitField('Login')