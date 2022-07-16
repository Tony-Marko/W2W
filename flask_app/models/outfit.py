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
        query = """SELECT * from outfits
                    # LEFT JOIN users on users.id = outfits.user_id
                    # WHERE user.id = %(user_id)s;"""
        result = connectToMySQL(db).query_db(query,data)
        all_outfits = []
        for item in result:
            all_outfits.append(cls(item))
        print("Get all result is", all_outfits)
        return all_outfits
        

        

#     @classmethod #edit items
#     def edit_item(cls, data):
#         #images removed from edit for now. Image code: , image %(image)s
#         query = """UPDATE items SET name = %(name)s, category =%(category)s, type = %(type)s, brand = %(brand)s, size = %(size)s, color = %(color)s, price = %(price)s WHERE id = %(id)s;"""
#         result = connectToMySQL(db).query_db(query,data)
#         print ("EEEDDDDIIITTT result", result)
#         return result

#     @classmethod #delete an item
#     def delete_item(cls, data):
#         query = """DELETE FROM items where id = %(id)s"""
#         result = connectToMySQL(db).query_db(query,data)
#         print ("DDDEEELLLEEETTEEE result", result)
#         return result



#     @staticmethod
#     def parsed_validate_data(data):
#         parsed_data = {}
#         parsed_data['name'] = data['name']
#         parsed_data['category'] = data['category']
#         parsed_data['brand'] = data['brand']
#         return parsed_data      

#     @staticmethod
#     def parsed_all_data(data):
#         parsed_data = {}
#         parsed_data['name'] = data['name']
#         parsed_data['category'] = data['category']
#         parsed_data['type'] = data['type']
#         parsed_data['brand'] = data['brand']
#         parsed_data['size'] = data['size']
#         parsed_data['color'] = data['color']
#         parsed_data['price'] = int(data['price'])
#         parsed_data['image'] = NULL
#         parsed_data['profile_id'] = data['profile_id']
#         return parsed_data      

#     @staticmethod
#     def parsed_edit_data(data):
#         parsed_data = {}
#         parsed_data['id'] = data['id']
#         parsed_data['name'] = data['name']
#         parsed_data['category'] = data['category']
#         parsed_data['type'] = data['type']
#         parsed_data['brand'] = data['brand']
#         parsed_data['size'] = data['size']
#         parsed_data['color'] = data['color']
#         parsed_data['price'] = int(data['price'])
#         #images removed for now
#         return parsed_data      