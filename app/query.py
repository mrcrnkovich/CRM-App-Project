'''
This is a helper module to look up users, clients, showings, properties
with a consistent query naming convention.
'''
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

def getUserById(id):
	return db.session.query(User).filter(User.id==id).first()

def getUserByEmail(email):
	return db.session.query(User).filter(User.email==email).first()

def getShowingById(id):
	return db.session.query(Showings).filter(Showings.showings_id==id).first()

def getShowingByUser(username):
	return db.session.query(Showings).join(Client).join(User).filter(User.username==username).all()

def getShowingByClient(client):
	return db.session.query(Showings).join(Client).filter(Client.id==client).all()
"""
def getPropertyById(id):
	return db.session.query(Properties).filter(Properties.Property_ID==id).first()


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