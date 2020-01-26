# app/auth/views.py

from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from app import db, http_auth
from auth.forms import LoginForm, RegistrationForm
from app.models import User


@auth.route('/auth', methods=['GET', 'POST'])
def register():

    # Render the homepage template on the / route
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(username=form.username.data,
                email=form.email.data)
        user.password(form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('You are registered')

        return redirect(url_for('auth.login'))

    return render_template('auth/register.html', title="Register", form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    # on submit, go to database, check user exists, verify password, log-in.
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()
        if verify_login(user,
                form.password.data):
            login_user(user)
            return redirect(url_for('home.dashboard'))
        else:
            flash('Invalid email or password')

    return render_template('auth/login.html', title="Login", form=form)


@http_auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(email=username).first()
    return verify_login(user, password)


def verify_login(user, password):
    return (user and user.check_password(password))
