# home/forms.py

from flask_wtf import FlaskForm
from wtforms import  IntegerField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo


class AddClientForm(FlaskForm):

    # Log users in

    email = StringField('Email Address',
                validators=[DataRequired(), Email()])
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    phone = StringField('Phone Number', 
                validators=[DataRequired()])
    submit = SubmitField('Add Client')

class AddShowingForm(FlaskForm):
   
    # Form set-up to add new showings

    client_id = IntegerField('Client ID')
    Property_ID = IntegerField('Property ID')
    Feedback = StringField('Feedback') 
    Rating =  IntegerField('Rating')
    submit = SubmitField('Submit')

class AddPropertyForm(FlaskForm):
    prop_id = IntegerField("Property ID",
                validators=[DataRequired()])
    list_price = IntegerField("List Price",
                validators=[DataRequired()])
    location = StringField("Property Location",
                validators=[DataRequired()])
    trend_link = StringField("Property Link")
    submit = SubmitField("Add Property")

class AddSearchForm(FlaskForm):
    search = StringField("Search")
    submit = SubmitField("Submit")

