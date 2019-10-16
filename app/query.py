'''
This is a helper module to look up users, clients, showings, properties
with a consistent query naming convention.
'''
from collections import namedtuple
from app import db
from app.models import Client, User, Showings, Properties, Contracts


def getClientById(id):
	return db.session.query(Client).filter(Client.id==id).first()

def getClientByEmail(email):
	return db.session.query(Client).filter(Client.email==email).first()

def getClientsForUserId(user_id):
	return db.session.query(Client).filter(Client.user_id==user_id).all()

def getClientsForUser(username):
	return db.session.query(Client).join(User).filter(User.username==username).all()

def getUsers():
	return db.session.query(User).all()

def getUserById(id):
	return db.session.query(User).filter(User.id==id).first()

def getUserByName(username):
	return db.session.query(User).filter(User.username==username).first()

def getUserByEmail(email):
	return db.session.query(User).filter(User.email==email).first()

def getShowingById(id):
	s = db.session.query(Showings, Client, User, Properties).\
		join(Client, Client.id == Showings.client_id).\
		join(User, Client.user_id==User.id).\
		join(Properties, Properties.Property_ID==Showings.Property_ID).\
		filter(Showings.showing_id==id).all()
	return [{**x[0].json(), **x[1].json(), **x[2].json(), **x[3].json()} for x in s]

def getShowingByUser(username):
	s = db.session.query(Showings, Client, Properties).\
		join(Client, Client.id == Showings.client_id).\
		join(User, Client.user_id==User.id).\
		join(Properties, Properties.Property_ID==Showings.Property_ID).\
		filter(User.username==username).all()
	return [{**x[0].json(), **x[1].json(), **x[2].json()} for x in s]
			

def getShowingByClient(client):
	s = db.session.query(Showings, Properties).\
		join(Client, Client.id == Showings.client_id).\
		join(User, Client.user_id==User.id).\
		join(Properties, Properties.Property_ID==Showings.Property_ID).\
		filter(Client.id==client).all()
	return [{**x[0].json(), **x[1].json()} for x in s]

def getShowings():
	s = db.session.query(Showings, Client, User, Properties).\
		join(Client, Client.id == Showings.client_id).\
		join(User, Client.user_id==User.id).\
		join(Properties, Properties.Property_ID==Showings.Property_ID).all()
	return [{**x[0].json(), **x[1].json(), **x[2].json(), **x[3].json()} for x in s]

def getPropertyById(id):
	return db.session.query(Properties).filter(Properties.Property_ID==id).first()

def getProperties():
	prop = db.session.query(Properties).all()
	return ({"Properties":[p.json() for p in prop]})
"""
def createClient(client):
	try:
	    db.session.add(Client(first_name=client['first_name'],
	                            last_name=client['last_name'],
	                            email=client['email'],
	                            phone=client['phone'],
	                            user_id=client['user_id']))
	    db.session.commit()

	except:
		return
"""