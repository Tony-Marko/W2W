from asyncio.windows_events import NULL
from flask_app import app
from flask import render_template, redirect, request, session, flash

from flask_app.models import item
from flask_app.models.profile import Profile

# //////READ////////
@app.route("/wardrobe")
def wardrobe():
    if 'user_id' not in session:
        flash("Please log back in")
        return redirect ('/')
    return render_template ('wardrobe.html')

@app.route("/additem")
def additem():
    if 'user_id' not in session:
        flash("Please log back in")
        return redirect ('/')
    return render_template ('additem.html')

#/////////////////////////
@app.route("/showitem")
def myitems():
    if 'user_id' not in session:
        flash("Please log back in")
        return redirect ('/')
    data = {"user_id" : session['user_id'] }
    all_items = item.Item.get_all_items_by_user_id(data)
    gotitem = NULL
    return render_template ("showitem.html", all_items = all_items, gotitem=gotitem)
#/////////////////////////////

@app.route("/showitem/<id>", methods = ['post', 'get'])
def showitem(id):
    if 'user_id' not in session:
        flash("Please log back in")
        return redirect ('/')
    data = {"id" : id }
    gotitem = item.Item.get_item_by_id(data)
    return render_template ("showitem.html", gotitem = gotitem)

@app.route("/outfits")
def outfits():
    if 'user_id' not in session:
        flash("Please log back in")
        return redirect ('/')
    return render_template ('outfits.html')

@app.route("/createoutfit")
def createoutfit():
    if 'user_id' not in session:
        flash("Please log back in")
        return redirect ('/')
    return render_template ('createoutfit.html')

@app.route("/randomize")
def randomize():
    if 'user_id' not in session:
        flash("Please log back in")
        return redirect ('/')
    return render_template ('randomize.html')

# ////////CREATE//////////
@app.route("/addnewitem", methods = ['post'])
def addnewitem():
    if 'user_id' not in session:
        flash("Please log back in")
        return redirect ('/')
    if not item.Item.validate(request.form):
        return redirect ("/additem")
    data = item.Item.parsed_all_data(request.form)
    newitem = item.Item.new_item(data)
    session['item_id'] = newitem
    newpage = f'/showitem/{newitem}'
    return redirect (newpage)


    


# @app.route('/process', methods = ['post'])
# def process():
#     if not Register.validate(request.form):
#         return redirect ('/register')
#     data = Register.parsed_data(request.form)
#     user_id = Register.new_user(data)
#     session['user_id'] = user_id
#     return redirect ('/profile')

# @app.route('/createprofile', methods = ['post'])
# def createprofile():
#     if not Profile.validate(request.form):
#         return redirect ('/profile')
#     data = Profile.parsed_data(request.form)
#     newprofile = Profile.new_profile(data)
#     return redirect ('/dashboard')

#login-register-profile works!

