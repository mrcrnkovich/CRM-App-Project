# app/auth/forms.py

from flask_wtf import FlaskForm
from wtforms import  StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo


class SearchForm(FlaskForm):

    # Log users in

    email = StringField('Email Address',
                validators=[DataRequired(), Email()])
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    phone = StringField('Phone Number', 
                validators=[DataRequired()])
    submit = SubmitField('Add Client')
