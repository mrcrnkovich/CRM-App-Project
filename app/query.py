'''
This is a helper module to look up users, clients, showings, properties
with a consistent query naming convention.
'''
from collections import namedtuple
from functools import reduce
from app import db
from app.models import Client, User, Showings, Properties, Contracts


# Do I return only client objects, or only jsons?? Do i add a json wrapper class,
# or is there a better way to handle this?

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
	return [{**x.json(), **y.json(), **z.json()} for x, y, z in s]
			

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



def createClient(client):
	try:
	    db.session.add(Client(first_name=client['first_name'],
	                            last_name=client['last_name'],
	                            email=client['email'],
	                            phone=client['phone'],
	                            user_id=client['user_id']))
	    db.session.commit()
	    return ("sucess")
	except:
		return (f"Could not add client: {client}")

def createShowing(showing):
	# try add showing to db except return value
	pass

def createProperty(property):
	#to do, try add property to db.
	pass

def updateClient(client):
	#to do, update client fields to db.
	pass

def updateShowing(showing):
	#to do, update client fields to db.
	pass

def updateProperty(property):
	#to do, update client fields to db.
	pass

# may end up using as decorator, not sure yet.
def jsonListToDict(l):
	return [reduce(lambda y,z: {**y, **z},
		list(map(lambda a: a.json(), x))) for x in l]