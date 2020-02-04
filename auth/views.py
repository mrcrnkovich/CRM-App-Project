# app/auth/views.py

from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from app import db, http_auth
from auth.forms import LoginForm, RegistrationForm
from app.models import User

@auth.route('/login', methods=['GET', 'POST'])
def login():

    # Render the homepage template on the / route
    register_form = RegistrationForm()

    if register_form.validate_on_submit():
        user = User(username=register_form.username.data,
                email=register_form.email.data)
        user.password(register_form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('You are registered')

        return redirect(url_for('auth.login'))

    # on submit, go to database, check user exists, verify password, log-in.
    login_form = LoginForm()

    if login_form.validate_on_submit():

        user = User.query.filter_by(email=login_form.email.data).first()
        if verify_login(user,
                login_form.password.data):
            login_user(user)
            return redirect(url_for('home.dashboard'))
        else:
            flash('Invalid email or password')

    return render_template('auth/login.html', title="Login",
                register_form=register_form, login_form=login_form)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.homepage'))


@http_auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(email=username).first()
    return verify_login(user, password)


def verify_login(user, password):
    return (user and user.check_password(password))
