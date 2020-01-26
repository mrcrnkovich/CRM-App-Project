# app/auth/__init_.py

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views
