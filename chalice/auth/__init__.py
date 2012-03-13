from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask.ext.login import current_user, login_required, login_user, logout_user, confirm_login
from chalice.extensions import lm
from chalice.auth.models import User
from sqlalchemy import and_

auth = Blueprint('auth', __name__, template_folder = 'templates')

lm.login_view = 'auth.login'
lm.login_message = u'Please log in to access this page.'
lm.refresh_view = 'auth.reauth'

@lm.user_loader
def load_user(uid):
    return User.query.get(int(uid))

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form:
        uname = request.form['username']
        upass = request.form['password']
        user = User.query.filter(and_(User.name == uname, User.password == upass)).first()
        if user:
            remember = request.form.get('remember', 'no') == 'yes'
            if login_user(user, remember = remember):
                return redirect(request.args.get('next') or url_for('blog.show_posts'))
            else:
                flash('Could not log you in for some strange reason')
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@auth.route('/reauth', methods = ['GET', 'POST'])
def reauth():
    if request.method == 'POST':
        confirm_login()
        return redirect(request.args.get('next') or url_for('blog.show_posts'))
    return render_template('reauth.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('blog.show_posts'))
