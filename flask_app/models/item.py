from asyncio.windows_events import NULL
from flask import flash
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
#from datetime import date //to be used for last worn section

db = 'w2w'

class Item:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.category = data['category']
        self.type = data['type']
        self.brand = data['brand']
        self.size = data['size']
        self.color = data['color']
        self.price = data['price']
        self.image = data['image']
        self.user_id = data['user_id']


    @classmethod  #new item maker 
    def new_item(cls, data):
        # print("*******", data)
        query = """INSERT INTO items (name, category, type, brand, size, color, price, image, user_id)
                VALUES (%(name)s, %(category)s, %(type)s, %(brand)s, %(size)s, %(color)s, %(price)s, %(image)s, %(user_id)s);
                """
        result = connectToMySQL(db).query_db(query,data)
        print ("Result is", result)
        return (result)

    @classmethod #get all user's item
    def get_all_items_by_user_id(cls,data):
        query = """SELECT * from items
                    # LEFT JOIN users on users.id = items.user_id
                    # WHERE user.id = %(user_id)s;"""
        result = connectToMySQL(db).query_db(query,data)
        all_items = []
        for item in result:
            all_items.append(cls(item))

        return all_items
        

    @classmethod #get an item
    def get_item_by_id(cls, data):
        query = """SELECT * from items
                    WHERE id = %(id)s;"""
        result = connectToMySQL(db).query_db(query,data)
        # print (result)
        return cls(result[0])

    @classmethod #get an item
    def get_item_for_outfit(cls, data):
        if data == 0:
            return "None"
        data = {"id" : data}
        query = """SELECT * from items
                    WHERE id = %(id)s;"""
        result = connectToMySQL(db).query_db(query,data)
        # print (result)
        return cls(result[0])

    @classmethod #edit items
    def edit_item(cls, data):
        #images removed from edit for now. Image code: , image %(image)s
        query = """UPDATE items SET name = %(name)s, category =%(category)s, type = %(type)s, brand = %(brand)s, size = %(size)s, color = %(color)s, price = %(price)s WHERE id = %(id)s;"""
        result = connectToMySQL(db).query_db(query,data)
        print ("EEEDDDDIIITTT result", result)
        return result

    @classmethod #delete an item
    def delete_item(cls, data):
        query = """DELETE FROM items where id = %(id)s"""
        result = connectToMySQL(db).query_db(query,data)
        print ("DDDEEELLLEEETTEEE result", result)
        return result

#////// methods for outfits
    @classmethod
    def get_headwear(cls, data):
        query = """SELECT * FROM items
                JOIN users on users.id = items.user_id
                WHERE category LIKE 'headwear' and users.id =%(user_id)s;"""
        result = connectToMySQL(db).query_db(query,data)
        all_headwear = []
        for item in result:
            all_headwear.append(cls(item))
        # print("Get all headwear result is", all_headwear)
        return all_headwear

    @classmethod
    def get_top(cls, data):
        query = """SELECT * FROM items
                JOIN users on users.id = items.user_id
                WHERE category LIKE 'top' and users.id =%(user_id)s;"""
        result = connectToMySQL(db).query_db(query,data)
        all_top = []
        for item in result:
            all_top.append(cls(item))
        # print("Get all TOP result is", all_top)
        return all_top

    @classmethod
    def get_waist(cls, data):
        query = """SELECT * FROM items
                JOIN users on users.id = items.user_id
                WHERE category LIKE 'waist' and users.id =%(user_id)s;"""
        result = connectToMySQL(db).query_db(query,data)
        all_waist = []
        for item in result:
            all_waist.append(cls(item))
        # print("Get all WAIST result is", all_waist)
        return all_waist

    @classmethod
    def get_bottom(cls, data):
        query = """SELECT * FROM items
                JOIN users on users.id = items.user_id
                WHERE category LIKE 'bottom' and users.id =%(user_id)s;"""
        result = connectToMySQL(db).query_db(query,data)
        all_bottom = []
        for item in result:
            all_bottom.append(cls(item))
        # print("Get all BOTTOM result is", all_bottom)
        return all_bottom

    @classmethod
    def get_footwear(cls, data):
        query = """SELECT * FROM items
                JOIN users on users.id = items.user_id
                WHERE category LIKE 'footwear' and users.id =%(user_id)s;"""
        result = connectToMySQL(db).query_db(query,data)
        all_footwear = []
        for item in result:
            all_footwear.append(cls(item))
        # print("Get all FOOTWEAR result is", all_footwear)
        return all_footwear
        
    @classmethod
    def get_accessory(cls, data):
        query = """SELECT * FROM items
                JOIN users on users.id = items.user_id
                WHERE category LIKE 'accessory' and users.id =%(user_id)s;"""
        result = connectToMySQL(db).query_db(query,data)
        all_accessory = []
        for item in result:
            all_accessory.append(cls(item))
        # print("Get all ACCESSORY result is", all_accessory)
        return all_accessory


    @staticmethod
    def validate(newitem):
        is_valid = True
        #item name
        if len(newitem['name'])<1:
            flash("Please name your new item", 'itemerror')
            is_valid = False        
        #category
        if len(newitem['category'])=="":
            flash("Please select a category", 'itemerror')
            is_valid = False
        #country
        if (newitem["brand"])=="":
            flash("Please enter a brand name (enter: 'Unknown' if you don't know)", "itemerror")
            is_valid = False
        return is_valid


    @staticmethod
    def parsed_validate_data(data):
        parsed_data = {}
        parsed_data['name'] = data['name']
        parsed_data['category'] = data['category']
        parsed_data['brand'] = data['brand']
        return parsed_data      

    @staticmethod
    def parsed_all_data(data):
        parsed_data = {}
        parsed_data['name'] = data['name']
        parsed_data['category'] = data['category']
        parsed_data['type'] = data['type']
        parsed_data['brand'] = data['brand']
        parsed_data['size'] = data['size']
        parsed_data['color'] = data['color']
        parsed_data['price'] = int(data['price'])
        parsed_data['image'] = NULL
        parsed_data['user_id'] = data['user_id']
        return parsed_data      

    @staticmethod
    def parsed_edit_data(data):
        parsed_data = {}
        parsed_data['id'] = data['id']
        parsed_data['name'] = data['name']
        parsed_data['category'] = data['category']
        parsed_data['type'] = data['type']
        parsed_data['brand'] = data['brand']
        parsed_data['size'] = data['size']
        parsed_data['color'] = data['color']
        parsed_data['price'] = int(data['price'])
        #images removed for now
        return parsed_data      