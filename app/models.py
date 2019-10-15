from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager

class User(db.Model, UserMixin):

	#create User table

	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))

	@property
	def password(self):
		raise AttributeError('password is not a readable attribute.')

	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash , password)	

	def __repr(self):
		return f'<User: {self.username}>'

	def json(self):
		return ({"username":self.username,
				"email":self.email})

class Client(db.Model):

	__tablename__ = 'clients'


	#unique client id
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(16), index=True)
	last_name = db.Column(db.String(32), index=True)
	email = db.Column(db.String(128), index=True, unique=True)
	phone = db.Column(db.String(16))

	#link to users table
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	user = db.relationship('User', backref=db.backref('Client', lazy=True))
	

	def __repr(self):
		return f"<Client {self.last_name}, {self.first_name}>"

	def json(self):
		return	({"first_name":self.first_name,
	    		"last_name":self.last_name,
	    		"email":self.email,
	    		"phone":self.phone})



class Contracts(db.Model):
	
	__tablename__ = 'contracts'

	trans_id = db.Column(db.Integer, primary_key=True)
	
	client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
	client = db.relationship('Client', backref=db.backref('Contracts', lazy=True))
	Property_ID=db.Column(db.Integer, db.ForeignKey('properties.Property_ID'))
	properties = db.relationship('Properties', backref=db.backref("Contracts", lazy=True))

	price = db.Column(db.Integer)
	location = db.Column(db.String(128))

	day_zero = db.Column(db.DateTime, nullable=False, 
		default=datetime.utcnow())
	deposit_first = db.Column(db.Integer) 
	deposit_second = db.Column(db.Integer) 
	BRI_day = db.Column(db.Integer) 
	closing_day = db.Column(db.Integer)


	def __repr(self):
		return f"<Contract: {self.location}"

	def json(self):
		return ({"trans_id":self.trans_id,
				"client_id":self.client_id,
				"price":self.price,
				"location":self.location,
				"day_zero":self.day_zero,
				"deposit_first":self.deposit_first,
				"deposit_second":self.deposit_second,
				"bri_day":self.BRI_day,
				"closing_day":self.closing_day})


class Properties(db.Model):

	__tablename__= "properties"

	#property id should be trend mls id also
	Property_ID= db.Column(db.Integer, primary_key=True)
	List_Price= db.Column(db.Integer)
	Location = db.Column(db.String(128))
	Trend_Link = db.Column(db.String(128))

	def __repr(self):
		return f"<Property: {self.Location}>"

	def json(self):
		return	({"Property_ID":self.Property_ID,
	    		"List_Price":self.List_Price,
	    		"Location":self.Location,
	    		"Link":self.Trend_Link})

class Showings(db.Model):

	__tablename__ = 'showings'

	showing_id = db.Column(db.Integer, primary_key=True)
	client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
	client = db.relationship('Client', backref=db.backref('Showings', lazy=True))
	Property_ID=db.Column(db.Integer, db.ForeignKey('properties.Property_ID'))
	properties = db.relationship('Properties', backref=db.backref("Showings", lazy=True))
	Feedback = db.Column(db.String(255))
	Rating= db.Column(db.Integer)

	def __repr(self):
		return f"<Showing: {self.Property_ID}, Rating: {self.Rating}>"

	def json(self):
		return ({"Showing_id":self.showing_id,
				"Client_id":self.client_id,
				"Property_ID":self.Property_ID,
				"Feedback":self.Feedback,
				"Rating":self.Rating})



from app import query
#Load user_login
@login_manager.user_loader
def load_user(user_id):
	return query.getUserById(int(user_id))