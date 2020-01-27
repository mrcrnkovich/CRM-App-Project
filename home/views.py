# app/home/views.py

from flask import render_template
from flask_login import login_required, current_user
from . import home
from app import query
from home.forms import SearchForm

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")


@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """

    print(query.getClientsForUser(current_user.username))

    # on submit re-render template using form data and query


    form = SearchForm()
    return render_template('home/dashboard.html',
        title="Dashboard", user=current_user, form=form)

