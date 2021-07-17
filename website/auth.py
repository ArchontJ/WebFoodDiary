from flask import Blueprint
from flask.templating import render_template

auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return render_template('login.html',text="Testing", user="Archu")

@auth.route('/logout')
def logout():
    return render_template('home.html')

@auth.route('/sign-up')
def sign_up():
    return render_template('signup.html')