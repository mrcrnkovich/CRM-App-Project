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


@home.route('/dashboard',methods=['GET', 'POST'])
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """

    form = SearchForm()
    showings = query.getShowingByUser(current_user.username)
    table = query.getClientsForUser(current_user.username)
    print(current_user.id)
    # on submit re-render template using form data and query
    if form.validate_on_submit():
    
        query.createClient({
            'first_name': form.client_name.data,
            'last_name': form.client_name.data,
            'email': form.email.data,
            'phone': '111-222-3344',
            'user_id': current_user.id
            })

        table = query.getClientsForUser(current_user.username)

        return render_template('home/dashboard.html',
                title="reload", table=table, user=current_user,
                form=form, showings=showings)

    return render_template('home/dashboard.html',
        title="Dashboard", table=table, user=current_user, form=form)

