from asyncio.windows_events import NULL
from flask import flash
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
#from datetime import date //to be used for last worn section

db = 'w2w'

class Outfit:
    def __init__(self, data):
        self.id = data['id']
        self.headwear = data['headwear']
        self.top = data['top']
        self.waist = data['waist']
        self.bottom = data['bottom']
        self.footwear= data['footwear']
        self.acc1 = data['acc1']
        self.acc2 = data['acc2']
        self.user_id = data['user_id']


#     @classmethod  #new item maker 
#     def new_item(cls, data):
#         # print("*******", data)
#         query = """INSERT INTO items (name, category, type, brand, size, color, price, image, profile_id)
#                 VALUES (%(name)s, %(category)s, %(type)s, %(brand)s, %(size)s, %(color)s, %(price)s, %(image)s, %(profile_id)s);
#                 """
#         result = connectToMySQL(db).query_db(query,data)
#         print ("Result is", result)
#         return (result)

#     @classmethod #get all user's item
#     def get_all_items_by_user_id(cls,data):
#         query = """SELECT * from items
#                     # LEFT JOIN users on users.id = profiles.user_id
#                     # JOIN items on items.profile_id = profiles._id
#                     # WHERE user.id = %(user_id)s;"""
#         result = connectToMySQL(db).query_db(query,data)
#         all_items = []
#         for item in result:
#             all_items.append(cls(item))
#         print("Get all result is", all_items)
#         return all_items
        

#     @classmethod #get an item
#     def get_item_by_id(cls, data):
#         query = """SELECT * from items
#                     WHERE id = %(id)s;"""
#         result = connectToMySQL(db).query_db(query,data)
#         print (result)
#         return cls(result[0])

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
#     def validate(newitem):
#         is_valid = True
#         #item name
#         if len(newitem['name'])<1:
#             flash("Please name your new item", 'itemerror')
#             is_valid = False        
#         #category
#         if len(newitem['category'])=="":
#             flash("Please select a category", 'itemerror')
#             is_valid = False
#         #country
#         if (newitem["brand"])=="":
#             flash("Please enter a brand name (enter: 'Unknown' if you don't know)", "itemerror")
#             is_valid = False
#         return is_valid


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