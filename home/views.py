# app/home/views.py

from flask import render_template
from flask_login import login_required, current_user
from . import home
from app import query
from home.forms import AddClientForm, AddPropertyForm 

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")


@home.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """

    client_form = AddClientForm()
    prop_form = AddPropertyForm()
    showings = query.getShowingByUser(current_user.username)
    table = query.getClientsForUser(current_user.username)
    
    # on submit re-render template using form data and query
    if client_form.validate_on_submit():

        query.createClient({
            'first_name': form.first_name.data,
            'last_name': form.last_name.data,
            'email': form.email.data,
            'phone': form.phone.data,
            'user_id': current_user.id
            })

        table = query.getClientsForUser(current_user.username)

        return render_template('home/dashboard.html',
                title="reload", table=table, user=current_user,
                form=form, showings=showings)

    return render_template('home/dashboard.html',
        title="Dashboard", table=table, user=current_user,
        showings=showings, client_form=client_form, prop_form=prop_form)

