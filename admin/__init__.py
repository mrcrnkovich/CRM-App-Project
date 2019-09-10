#app/admin/__init_.py

from flask import Blueprint

admin = Blueprint('admin', __name__)

from . import views