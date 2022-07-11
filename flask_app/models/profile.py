import string
from flask import flash
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from datetime import date

db = 'w2w'

class Profile:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['first_name']
        self.password = data['last_name']
        self.birthday = data['birthday']
        self.country = data['country']
        self.user_id = data['user_id']

    @classmethod  #new profile maker 
    def new_profile(cls, data):
        print("*******", data)
        query = """INSERT INTO profiles (first_name, last_name, birthday, country)
                VALUES (%(first_name)s, %(last_name)s, %(birthday)s. %(country)s);
                """
        result = connectToMySQL(db).query_db(query,data)
        print (result)
        return result

    @classmethod #get user's profile
    def get_profile_by_id(data):
        query = """SELECT * from profiles
                    LEFT JOIN users on users.id = profiles.user_id
                    WHERE user_id = %(user_id)s;"""


    @staticmethod
    def validate(newuser):
        print(("**************", newuser["birthday"]))
        is_valid = True
        #firts_name
        if len(newuser['first_name'])<1:
            flash("Please enter your first name", 'profileerror')
            is_valid = False
        #last_name
        if len(newuser['last_name'])<1:
            flash("Please enter your last name", 'profileerror')
            is_valid = False        
        #birthday
        if (newuser["birthday"])=="":
            flash("Please enter your birthdate", "profileerror")
            is_valid = False
        else: 
            if (date.fromisoformat(newuser['birthday'])) >= date.today():
                flash("Birthdate cannot be today or the future", "profileerror")
                is_valid = False
        #country
        if (newuser["country"])=="":
            flash("Please select your country or residence", "profileerror")
            is_valid = False
        return is_valid


    @staticmethod
    def parsed_data(data):
        parsed_data = {}
        parsed_data['first_name'] = data['first_name']
        parsed_data['last_name'] = data['last_name']
        parsed_data['birthday'] = data['birthday']
        parsed_data['country'] = data['country']
        parsed_data['user_id'] = data['user_id']
        return parsed_data        


