# app/admin/views.py

from flask import render_template
from flask_login import login_required

from . import admin
from admin.forms import LoginForm, RegistrationForm

@admin.route('/admin')
def homepage():
    """
    Render the homepage template on the / route
    """
    form = LoginForm()
    return render_template('admin/index.html', title="Admin", form=form)


@admin.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('admin/dashboard.html', title="Dashboard")
