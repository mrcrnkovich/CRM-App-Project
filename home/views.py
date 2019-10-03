# app/home/views.py

import json
from flask import render_template, jsonify, make_response, request
from flask_login import login_required, current_user
from app.models import User

import pandas as pd
from bokeh.embed import file_html
from bokeh.resources import Resources

from . import home
from app import db
from app.dashboard import count_clients

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
    	table = table[['first_name','id_x']].to_html(classes = "table table-striped"), title="Dashboard")


@home.route('/other')
def other():
    return ("some stuff yet to be accomplished")


# testing method to be deleted upon completion
@home.route('/get_clients')
@login_required
def get_clients():
    return jsonify(pd.read_sql('clients', db.engine).to_json(orient="split", index=False))

# method to return clients by agent/username
@home.route('/<username>/get_clients')
@login_required
def get_some_clients(username, methods=['GET']):
    query = 'select clients.email, users.username, clients.first_name, clients.last_name from clients LEFT JOIN users ON users.id=clients.user_id;'
    data = pd.read_sql(query, db.engine)
    response = jsonify(data[data['username']==username].to_json(orient="split", index=False))
    return make_response(response)

#test for POST data from API to represent a new client
#add put method for clients, need to define format
@home.route('/<username>/add_clients', methods=['GET', 'POST'])
def add_clients(username):
    
    data = json.loads(request.data)
    for client in data["clients"]:
        addClient(client) # helper method to sanatize data, then add to database

    # update response to conform with general standards.
    return make_response("sucess"+"\n")

# Move this to separate module in Home for adding/modifiying clients
# client info passed as json {Field_Name:"data"}
def addClient(client):
    print("Adding client:")
    print(f"First Name is: {client['first_name']}")
    print(f"Last Name is: {client['last_name']}")