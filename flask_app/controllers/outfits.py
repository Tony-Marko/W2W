from asyncio.windows_events import NULL
from flask_app import app
from flask import render_template, redirect, request, session, flash

from flask_app.models import item, outfit

# # //////READ////////

@app.route("/myoutfits")
def myoutfits():
    if 'user_id' not in session:
        flash("Please log back in")
        return redirect ('/')
    data = {"user_id" : session['user_id'] }
    all_outfits = outfit.Outfit.get_all_outfits_by_user_id(data)
    gotoutfit = NULL
    return render_template ("myoutfits.html", all_outfits = all_outfits, gotoutfit=gotoutfit)

@app.route("/showmyoutfit", methods = ['post'])
def showmyoutfit():
    id = request.form['select'] 
    newpage = f'/myoutfit/{id}'
    return redirect (newpage)

@app.route("/myoutfit/<id>")
def myoutfit(id):
    if 'user_id' not in session:
        flash("Please log back in")
        return redirect ('/')
    data = {"id" : id }
    gotoutfit = outfit.Outfit.get_outfit_by_id(data)
    headwear = item.Item.get_item_for_outfit(gotoutfit.headwear)
    top = item.Item.get_item_for_outfit(gotoutfit.top)
    waist = item.Item.get_item_for_outfit(gotoutfit.waist)
    bottom = item.Item.get_item_for_outfit(gotoutfit.bottom)
    footwear = item.Item.get_item_for_outfit(gotoutfit.footwear)
    acc1 = item.Item.get_item_for_outfit(gotoutfit.acc1)
    acc2 = item.Item.get_item_for_outfit(gotoutfit.acc2)
    data = {"user_id" : session['user_id'] }
    all_outfits = outfit.Outfit.get_all_outfits_by_user_id(data)
    return render_template ("myoutfits.html", all_outfits = all_outfits, gotoutfit = gotoutfit, headwear =headwear, top = top, waist = waist, bottom = bottom, footwear = footwear, acc1 = acc1, acc2 =acc2)

@app.route("/createoutfit")
def createoutfit():
    if 'user_id' not in session:
        flash("Please log back in")
        return redirect ('/')
    data = {"user_id" : session['user_id'] }
    all_headwear = item.Item.get_headwear(data)
    all_top = item.Item.get_top(data)
    all_waist = item.Item.get_waist(data)
    all_bottom = item.Item.get_bottom(data)
    all_footwear = item.Item.get_footwear(data)
    all_accessory = item.Item.get_accessory(data)
    return render_template ('createoutfit.html', all_headwear = all_headwear, all_top=all_top, all_waist= all_waist, all_bottom = all_bottom, all_footwear = all_footwear, all_accessory = all_accessory)


#///////// addnewoutfit
@app.route("/addnewoutfit", methods=['post'])
def addnewoutfit():
    new_outfit = outfit.Outfit.addnewoutfit(request.form)
    return redirect ("/myoutfits")

#Result from first outfit saved
# Running Query: INSERT INTO outfits (headwear, top, waist, bottom, footwear, acc1, acc2, user_id)
#                 VALUES ('3', '13', '14', '18', '22', '26', '0', '1');

# Result is 1

# @app.route("/showitem")
# def myitems():
#     if 'user_id' not in session:
#         flash("Please log back in")
#         return redirect ('/')
#     data = {"user_id" : session['user_id'] }
#     all_items = item.Item.get_all_items_by_user_id(data)
#     gotitem = NULL
#     return render_template ("showitem.html", all_items = all_items, gotitem=gotitem)

# @app.route("/showitempost", methods = ['post'])
# def showitempost():
#     id = request.form['select'] 
#     newpage = f'/showitem/{id}'
#     return redirect (newpage)

# @app.route("/showitem/<id>")
# def showitem(id):
#     if 'user_id' not in session:
#         flash("Please log back in")
#         return redirect ('/')
#     print ("$$$$ ID is", id, "ID TYPE is", type(id))
#     if id == "reject":
#         #add flash message
#         return redirect ('/showitem')
#     data = {"id" : id }
#     gotitem = item.Item.get_item_by_id(data)
#     data = {"user_id" : session['user_id'] }
#     all_items = item.Item.get_all_items_by_user_id(data)
#     return render_template ("showitem.html", all_items = all_items, gotitem = gotitem)

# @app.route("/edititem/<id>")
# def edititem(id):
#     if 'user_id' not in session:
#         flash("Please log back in")
#         return redirect ('/')
#     data = {"id" : id }
#     gotitem = item.Item.get_item_by_id(data)    
#     return render_template ("edititem.html", gotitem = gotitem)

# @app.route("/outfits")
# def outfits():
#     if 'user_id' not in session:
#         flash("Please log back in")
#         return redirect ('/')
#     return render_template ('outfits.html')

# @app.route("/createoutfit")
# def createoutfit():
#     if 'user_id' not in session:
#         flash("Please log back in")
#         return redirect ('/')
#     return render_template ('createoutfit.html')

# @app.route("/randomize")
# def randomize():
#     if 'user_id' not in session:
#         flash("Please log back in")
#         return redirect ('/')
#     return render_template ('randomize.html')

# # ////////CREATE//////////
# @app.route("/addnewitem", methods = ['post'])
# def addnewitem():
#     if 'user_id' not in session:
#         flash("Please log back in")
#         return redirect ('/')
#     if not item.Item.validate(request.form):
#         return redirect ("/additem")
#     data = item.Item.parsed_all_data(request.form)
#     newitem = item.Item.new_item(data)
#     session['item_id'] = newitem
#     newpage = f'/showitem/{newitem}'
#     return redirect (newpage)


# # ////////UPDATE///////////
# @app.route("/edityouritem", methods = ['post'])
# def edityouritem():
#     if not item.Item.validate(request.form):
#         return redirect ("/additem")
#     data = item.Item.parsed_edit_data(request.form)
#     edited_item = item.Item.edit_item(data)
#     pageid = request.form['id']
#     newpage = f'/showitem/{pageid}'
#     print("@@@@@@@ new page is" , newpage)
#     return redirect (newpage)
#     #note this does not include images, images removed from parsed data

# # ////////DELETE///////////
# # note: add flash messages to confirm deletions
# @app.route("/deleteitem/<id>")
# def deleteitem(id):
#     data = {"id" : id }
#     deleted_item = item.Item.delete_item(data)
#     return redirect ("/showitem")

