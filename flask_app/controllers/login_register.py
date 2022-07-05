from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app) 

from flask_app.models.user import User
from flask_app.models.register import Register


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods = ['post'])
def register():
    if not Register.validate(request.form):
        return redirect ('/')
    data = Register.parsed_data(request.form)
    user_id = Register.new_user(data)
    session['user_id'] = user_id
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    return redirect ('/success')

@app.route('/login', methods = ['post'])
def login():
    data = {'email' : request.form['email']}
    user_in_db = User.get_user_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password", "loginmessage")
        return redirect ('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password", "loginmessage")
        return redirect ('/')
    session['user_id'] = user_in_db.id
    session['first_name'] = user_in_db.first_name
    session['last_name'] = user_in_db.last_name
    return redirect ('/success')
    
@app.route('/success')
def success():
    if 'user_id' not in session:
        flash("Please log back in")
        return redirect ('/')
    return render_template ('success.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect ('/')
