# app/home/views.py

from flask import flash, render_template, request, redirect, session
from flask_login import login_required, current_user
from . import home
from app import query
from home.forms import AddClientForm, AddShowingForm, AddPropertyForm, AddSearchForm, SelectFieldForm

@home.route("/")
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template("home/index.html", title="Welcome")


@home.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """

    client_form = AddClientForm(prefix='client_form')
    prop_form = AddPropertyForm(prefix='prop_form')
    showing_form = AddShowingForm(prefix='showing_form')
    showings = query.getShowingByUser(current_user.username)
    table = query.getClientsForUser(current_user.username)

    if prop_form.validate_on_submit() and prop_form.submit.data:
        query.createProperty({
            'List_Price': prop_form.list_price.data,
            'Location': prop_form.location.data,
            'Trend_Link': prop_form.trend_link.data})

        return redirect("dashboard")

    if showing_form.validate_on_submit() and showing_form.submit.data:
        
        r = query.createShowing({
            'client_id': showing_form.client_id.data,
            'Property_ID': showing_form.Property_ID.data,
            'Feedback': showing_form.Feedback.data,
            'Rating': showing_form.Rating.data})
        print(r)

        showings = query.getShowingByUser(current_user.username)

        return redirect("dashboard")

    # on submit re-render template using form data and query
    if client_form.validate_on_submit() and client_form.submit.data:

        query.createClient(
            {
                "first_name": client_form.first_name.data,
                "last_name": client_form.last_name.data,
                "email": client_form.email.data,
                "phone": client_form.phone.data,
                "user_id": current_user.id,
            }
        )

        table = query.getClientsForUser(current_user.username)

        return redirect("dashboard")

    return render_template(
        "home/dashboard.html",
        title="Dashboard",
        table=table,
        user=current_user,
        showings=showings,
        showing_form=showing_form,
        client_form=client_form,
        prop_form=prop_form,
    )


@home.route("/update/client", methods=["GET", "POST"])
@login_required
def updates():

    client_form = AddClientForm(prefix="client_form")
    prop_form = AddPropertyForm(prefix='prop_form')
    showing_form = AddShowingForm(prefix='showing_form')
    search_form = AddSearchForm(prefix="search_form")
    form_choice = SelectFieldForm(prefix="select_form") 

    if form_choice.validate_on_submit() and form_choice.submit.data:
        print(f"{form_choice.data}")
        session["updates"] = form_choice.data['field']
        return redirect("client")

    if search_form.validate_on_submit() and search_form.submit.data:
        client = query.getClientsByFirstName(current_user.id, search_form.search.data)
        if client:
            session["client"] = client[0].json()
        else:
            flash("Error, no client found")
        return redirect("client")

    if client_form.validate_on_submit() and client_form.submit.data:

        query.updateClient(
            session["client"]["id"],
            {
                "first_name": client_form.first_name.data,
                "last_name": client_form.last_name.data,
                "email": client_form.email.data,
                "phone": client_form.phone.data,
            },
        )

        session["client"] = None
        return redirect("client")

    if session.get("client"):
        client = session["client"]
        client_form.first_name.data = client["first_name"]
        client_form.last_name.data = client["last_name"]
        client_form.email.data = client["email"]
        client_form.phone.data = client["phone"]

    if not session.get("updates"):
        form = client_form
    else:
        d = {'property':prop_form, 'showing': showing_form, 'client': client_form}
        print(session.get("updates"))
        form = d[session["updates"]]

    return render_template("home/update.html",select=form_choice,
        form=form, search=search_form)
