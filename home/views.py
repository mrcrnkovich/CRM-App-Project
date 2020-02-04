# app/home/views.py

from flask import render_template
from flask_login import login_required, current_user
from . import home
from app import query
from home.forms import AddClientForm, AddShowingForm, AddPropertyForm 

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
    showing_form = AddShowingForm()
    showings = query.getShowingByUser(current_user.username)
    table = query.getClientsForUser(current_user.username)

    if prop_form.validate_on_submit():
        query.createProperty({
            'List_Price': prop_form.list_price.data,
            'Location': prop_form.location.data,
            'Trend_Link': prop_form.trend_link.data})


        return render_template('home/dashboard.html',
                title="reload", table=table, user=current_user,
                client_form=client_form, showings=showings,
                showing_form=showing_form, prop_form=prop_form)
    
    if showing_form.validate_on_submit():
        
        query.createShowing({
            'client_id': showing_form.client_id.data,
            'Property_ID': showing_form.Property_ID.data,
            'Feedback': showing_form.Feedback.data,
            'Rating': showing_form.Rating.data})

        showings = query.getShowingByUser(current_user.username)

        return render_template('home/dashboard.html',
                title="reload", table=table, user=current_user,
                client_form=client_form, showings=showings,
                showing_form=showing_form, prop_form=prop_form)

    # on submit re-render template using form data and query
    if client_form.validate_on_submit():

        query.createClient({
            'first_name': client_form.first_name.data,
            'last_name': client_form.last_name.data,
            'email': client_form.email.data,
            'phone': client_form.phone.data,
            'user_id': current_user.id
            })

        table = query.getClientsForUser(current_user.username)

        return render_template('home/dashboard.html',
                title="reload", table=table, user=current_user,
                client_form=client_form, showings=showings,
                showing_form=showing_form, prop_form=prop_form)

    return render_template('home/dashboard.html',
        title="Dashboard", table=table, user=current_user,
        showings=showings, showing_form=showing_form,
        client_form=client_form, prop_form=prop_form)

