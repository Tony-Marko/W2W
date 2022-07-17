from asyncio.windows_events import NULL
from flask import flash
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
#from datetime import date //to be used for last worn section
from flask_app.models import item

db = 'w2w'

class Outfit:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.headwear = data['headwear']
        self.top = data['top']
        self.waist = data['waist']
        self.bottom = data['bottom']
        self.footwear= data['footwear']
        self.acc1 = data['acc1']
        self.acc2 = data['acc2']
        self.user_id = data['user_id']

# //////////Create/////////////
    @classmethod  #new outfit maker. Note: images left out of query
    def addnewoutfit(cls, data):
        print("*******", data)
        query = """INSERT INTO outfits (name, headwear, top, waist, bottom, footwear, acc1, acc2, user_id)
                VALUES (%(name)s, %(headwear)s, %(top)s, %(waist)s, %(bottom)s, %(footwear)s, %(acc1)s, %(acc2)s, %(user_id)s);
                """
        result = connectToMySQL(db).query_db(query,data)
        print ("Result is", result)
        return (result)

#///////////READ//////////////
    @classmethod #get an item
    def get_outfit_by_id(cls, data):
        query = """SELECT * from outfits
                    WHERE id = %(id)s;"""
        result = connectToMySQL(db).query_db(query,data)
        print ("Result is", result)
        return cls(result[0])

    @classmethod #get all user's outfits
    def get_all_outfits_by_user_id(cls,data):
        query = """SELECT * from outfits WHERE user_id = %(user_id)s;"""

        result = connectToMySQL(db).query_db(query,data)
        all_outfits = []
        for item in result:
            all_outfits.append(cls(item))
        print("Get all result is", all_outfits)
        return all_outfits

    @classmethod
    def editoutfit(cls, data):
        query = """UPDATE outfits 
                    LEFT JOIN users on users.id = outfits.user_id 
                    SET name = %(name)s, headwear = %(headwear)s, top =%(top)s, waist = %(waist)s, bottom = %(bottom)s, footwear = %(footwear)s, acc1 = %(acc1)s, acc2 = %(acc2)s 
                    WHERE outfits.id = %(id)s and users.id = %(user_id)s;"""
        result = connectToMySQL(db).query_db(query,data)
        print ("EEEDDDDIIITTT result", result)
        return result

    @classmethod #delete an outfit
    def delete_outfit(cls, data):
        query = """DELETE FROM outfits where id = %(id)s;"""
        result = connectToMySQL(db).query_db(query,data)
        print ("DDDEEELLLEEETTEEE result", result)
        return result

    @staticmethod 
    def validate(newoutfit):
        is_valid = True
        count = 0
        if len(newoutfit['name'])<1:
            flash("Please name your outfit.", 'outfiterror')
            is_valid = False        
        #category
        if (newoutfit['headwear'])=='0':
            count += 1
        if (newoutfit['top'])=='0':
            count += 1
        if (newoutfit['waist'])=='0':
            count += 1
        if (newoutfit['bottom'])=='0':
            count += 1
        if (newoutfit['footwear'])=='0':
            count += 1
        if (newoutfit['acc1'])=='0':
            count += 1
        if (newoutfit['acc2'])=='0':
            count += 1
        if count>6:
            flash("Please select at least two items", "outfiterror")
            is_valid = False
        return is_valid

