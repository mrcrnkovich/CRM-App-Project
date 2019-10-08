from flask import request
from flask_restful import abort, Resource
from flask_restful.reqparse import RequestParser
import pandas as pd
import json
import sqlalchemy

from app import db
from app.models import Client, User, Properties_Shown


class Clients(Resource):
	# method to return clients by agent/username

	def get(self, username):
		abort_null_agent(username)
		clients = db.session.query(Client).join(User).filter(User.username==username).all()
		return ({"clients":[client.json() for client in clients]})

	#test for POST data from API to represent a new client
	# add put method for clients, need to define format
	
	def post(self, username):
	    
	    data = json.loads(request.data)
	    for client in data["clients"]:
	        addClient(username, client) # helper method to sanatize data, then add to database

	    # update response to conform with general standards.
	    return("sucess"+"\n")


# Move this to separate module in Home for adding/modifiying clients
# will need a method of cleaning/checking the data & catching errors.
def addClient(username, client):
    print("Adding client:")
    print(f"First Name is: {client['first_name']}")
    print(f"Last Name is: {client['last_name']}")
    client = Client(first_name=client['first_name'],
                            last_name=client['last_name'],
                            email=client['email'],
                            phone=client['phone'],
                            user_id=client['user_id'])
    db.session.add(client)
    db.session.commit()
    print("Client successfully added")
    return

"""
# move to global position
def verify(username, password):
    if not (username and password):
        return False
    user = User.query.filter_by(email=username).first()
    print(user)
    return user.check_password(password)
"""
def abort_null_agent(agent):
	if not db.session.query(User).filter_by(username=agent).first():
		abort(404, message=f"Error: Agent {agent} does not exist")


def abort_null_property(property_id):
	if not db.session.query(Properties_Shown).filter_by(Property_ID=property_id).first():
		abort(404, message=f"Property ID #{property_id} does not exist")

class Properties(Resource):

	def get(self,property_id):
		print ('works')
		abort_null_property(property_id)
		pass

	def post(self, property_id):
		pass

	def put(self, property_id):
		pass

	def delete(self, property_id):
		pass

class Agents (Resource):

	def get(self):
		agents = db.session.query(User).all()
		return ({"Agents":[{"Username":agent.username, "ID":agent.id} for agent in agents]})

	def post(self):
		pass

	def put(self, username):
		pass

	def delete(self, username):
		pass
