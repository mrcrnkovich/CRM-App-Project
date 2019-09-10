from flask import Flask
from flask_cors import CORS
from config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail, Message
from flask_bootstrap import Bootstrap


crm = Flask(__name__)
crm.config.from_object(Config)

mail = Mail (crm)
db = SQLAlchemy(crm)
migrate = Migrate(crm, db)
Bootstrap(crm)

CORS(crm)

login_manager = LoginManager(crm)
login_manager.login_message = "You must be logged in"
login_manager.login_view = "auth.login"

from app import models
from app import dashboard

from admin import admin as admin_blueprint
crm.register_blueprint(admin_blueprint, url_prefix='/admin')

from auth import auth as auth_blueprint
crm.register_blueprint(auth_blueprint)

from home import home as home_blueprint
crm.register_blueprint(home_blueprint)