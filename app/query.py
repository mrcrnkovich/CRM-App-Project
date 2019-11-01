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


# decorater to convert the multiple objects returned by joined sql queries to
# a json.
def toJson(func):
        def inner(*args, **kwargs):
                l = func(*args, **kwargs)
                if not isinstance(l, list):
                        raise TypeError()

                return [reduce(lambda y,z: {**y, **z},
		    list(map(lambda a: a.json(), x))) for x in l]
        return inner

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

@toJson
def getShowingById(id):
        return db.session.query(Showings, Client, User, Properties).\
		join(Client, Client.id == Showings.client_id).\
		join(User, Client.user_id==User.id).\
		join(Properties, Properties.Property_ID==Showings.Property_ID).\
		filter(Showings.showing_id==id).all()

@toJson
def getShowingByUser(username):
	return db.session.query(Showings, Client, Properties).\
		join(Client, Client.id == Showings.client_id).\
		join(User, Client.user_id==User.id).\
		join(Properties, Properties.Property_ID==Showings.Property_ID).\
		filter(User.username==username).all()
		
@toJson
def getShowingByClient(client):
	return db.session.query(Showings, Properties).\
		join(Client, Client.id == Showings.client_id).\
		join(User, Client.user_id==User.id).\
		join(Properties, Properties.Property_ID==Showings.Property_ID).\
		filter(Client.id==client).all()

@toJson
def getShowings():
	return db.session.query(Showings, Client, User, Properties).\
	        join(Client, Client.id == Showings.client_id).\
		join(User, Client.user_id==User.id).\
		join(Properties, Properties.Property_ID==Showings.Property_ID).all()

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
	try:
	        db.session.add(Showings(client_id=showing['client_id'],
	                            Property_ID=showing['Property_ID'],
	                            Feedback=showing['Feedback'],
	                            Rating=showing['Rating']))
	        db.session.commit()
	        return ("sucess")
	except:
		return (f"Could not add Showing: {showing}")

def createProperty(property):
	#to do, try add property to db.
        try:
	        db.session.add(Properties(List_Price=property['List_Price'],
	                            Location=property['Location'],
	                            Trend_Link=property['Trend_Link']))
	        db.session.commit()
	        return ("sucess")
        except:
	        return (f"Could not add Property: {property}")

def updateClient(client):
	#to do, update client fields to db.
	pass

def updateShowing(showing):
	#to do, update client fields to db.
	pass

def updateProperty(property):
	#to do, update client fields to db.
	pass


def deleteModel(model):
        try:
                db.session.delete(model)
                db.session.commit()
                return (f'Removed: {model}')
        except:
                return (f'Could not remove {model}')

