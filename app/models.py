from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

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
		return '<User: {}>'.format(self.username)

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
	user = db.relationship('User', backref=db.backref('client', lazy=True))
	

	def __repr__(self):
		return "<Client {}>".format(self.last_name)

#Load user_login
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class Under_Contract_Trans(db.Model):
	
	__tablename__ = 'under_contract_trans'

	trans_id = db.Column(db.Integer, primary_key=True)
	
	client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
	client = db.relationship('Client', backref=db.backref('Under_Contract_Trans', lazy=True))
	#Property_ID = db.Column(db.Integer, 
	#	db.ForeignKey('properties_shown.Property_ID'))

	price = db.Column(db.Integer)
	location = db.Column(db.String(128))

	day_zero = db.Column(db.DateTime, nullable=False, 
		default=datetime.utcnow())
	deposit_first = db.Column(db.Integer) 
	deposit_second = db.Column(db.Integer) 
	BRI_day = db.Column(db.Integer) 
	closing_day = db.Column(db.Integer)


	def __repr__(self):
		return "<Contract: {}".format(self.location)

class Properties_Shown(db.Model):
	#property id should be trend mls id also
	Property_ID= db.Column(db.Integer, primary_key=True)
	List_Price= db.Column(db.Integer)
	Location = db.Column(db.String(128))
	Trend_Link = db.Column(db.String(128))

	def __repr__(self):
		return "<Property: {}>".format(self.Location)
"""
class Showings(db.model):
	client_id
	Property_ID=db.Column()
	property
	Feedback
	Rating= db.Column(db.Integer)

	def __repr__(self):
		return "open"

"""