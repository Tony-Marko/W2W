from asyncio.windows_events import NULL
from flask import flash, request, session
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
import re
from datetime import date
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app) 

db = 'login_schema'

class Register:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']

    @classmethod
    def new_user(cls, data):
        print("*******", data)
        query = """INSERT INTO users (first_name, last_name, email, password)
                VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
                """
        result = connectToMySQL(db).query_db(query,data)
        print (result)
        return result

    @staticmethod
    def validate(newuser):
        is_valid = True
        #first name
        if len(newuser['first_name'])<1:
            flash("First name is required", 'error')
            is_valid = False
        #last name
        if len(newuser['last_name'])<1:
            flash("Last name is required", 'error')
            is_valid = False
        #email
        if not EMAIL_REGEX.match(newuser['email']):
            flash("Invalid email address", 'error')
            is_valid = False
        #password
        if len(newuser['password'])<8:
            flash("Password must be at least 8 characters", 'error')
            is_valid = False
        if str.islower(newuser['password']) == True:
            flash("Password must contain at least one uppercase character", 'error')
            is_valid = False
        if any([char.isdigit() for char in newuser['password']]) == False:
            flash("Password must contain at least one number", 'error')
            is_valid = False
        if newuser['password'] != newuser['confirm_password']:
            flash("Passwords do not match")
            is_valid = False
        return is_valid

    @staticmethod
    def parsed_data(data):
        parsed_data = {}
        parsed_data['first_name'] = data['first_name']
        parsed_data['last_name'] = data['last_name']
        parsed_data['email'] = data['email'].lower()
        parsed_data['password'] = bcrypt.generate_password_hash(data['password'])
        return parsed_data        


