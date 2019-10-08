# app/home/views.py

import json
from flask import render_template, jsonify, make_response, request
from flask_login import login_required, current_user
from flask_httpauth import HTTPBasicAuth
from app.models import User, Client

import pandas as pd
from bokeh.embed import file_html
from bokeh.resources import Resources

from . import home
from app import db
from app.dashboard import count_clients

authHTTP = HTTPBasicAuth()


@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")


@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """

    resource = Resources(mode='inline')

    table, plot = count_clients()

    return render_template('home/dashboard.html', plot = file_html(plot, resource), 
    	table = table[['first_name','id_x']].to_html(classes = "table table-striped"),
        title="Dashboard")
