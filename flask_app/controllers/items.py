from asyncio.windows_events import NULL
from flask_app import app
from flask import render_template, redirect, request, session, flash

from flask_app.models import item

# //////READ////////
@app.route("/additem")
def additem():
    if 'user_id' not in session:
        flash("Please log back in")
        return redirect ('/')
    return render_template ('additem.html')

@app.route("/showitem")
def myitems():
    if 'user_id' not in session:
        flash("Please log back in")
        return redirect ('/')
    data = {"user_id" : session['user_id'] }
    all_items = item.Item.get_all_items_by_user_id(data)
    gotitem = NULL
    return render_template ("showitem.html", all_items = all_items, gotitem=gotitem)

@app.route("/showitempost", methods = ['post'])
def showitempost():
    id = request.form['select'] 
    newpage = f'/showitem/{id}'
    return redirect (newpage)

@app.route("/showitem/<id>")
def showitem(id):
    if 'user_id' not in session:
        flash("Please log back in")
        return redirect ('/')
    data = {"id" : id }
    gotitem = item.Item.get_item_by_id(data)
    data = {"user_id" : session['user_id'] }
    all_items = item.Item.get_all_items_by_user_id(data)
    return render_template ("showitem.html", all_items = all_items, gotitem = gotitem)

@app.route("/edititem/<id>")
def edititem(id):
    if 'user_id' not in session:
        flash("Please log back in")
        return redirect ('/')
    data = {"id" : id }
    gotitem = item.Item.get_item_by_id(data)    
    return render_template ("edititem.html", gotitem = gotitem)
    
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


# ////////UPDATE///////////
@app.route("/edityouritem", methods = ['post'])
def edityouritem():
    pageid = request.form['id']
    if not item.Item.validate(request.form):
        newpage = f'/edititem/{pageid}'
        return redirect (newpage)
    data = item.Item.parsed_edit_data(request.form)
    edited_item = item.Item.edit_item(data)
    newpage = f'/showitem/{pageid}'
    # print("@@@@@@@ new page is" , newpage)
    return redirect (newpage)
    #note this does not include images, images removed from parsed data

# ////////DELETE///////////
# note: add flash messages to confirm deletions
@app.route("/deleteitem/<id>")
def deleteitem(id):
    data = {"id" : id }
    deleted_item = item.Item.delete_item(data)
    flash("Item has been deleted", "delete")
    return redirect ("/showitem")

