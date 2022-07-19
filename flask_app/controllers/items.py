from asyncio.windows_events import NULL
from distutils.command.upload import upload
from flask_app import app
from flask_app.models import item
from flask import render_template, redirect, request, session, flash #, url_for
# import os
#code to upload files, might need to import Flask from flask
# from werkzeug.utils import secure_filename
# UPLOAD_FOLDER = '/path/to/the/uploads'
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# # app.config['MAX_CONTENT_PATH'] #use this to specify max file size


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
    if not item.Item.validate(request.form): #first we validata the data
        return redirect ("/additem")
    # print("#########", request.files)
    # newurl = f"/img/{request.form['user_id']}/{request.form['category']}" #then we create where to save the image
    # print("#########", newurl)

    # newfilename = upload.upload_file(newurl, request.files) #upload the file, return the filename
    # request.form['image'] = newfilename
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
@app.route("/deleteitem/<id>")
def deleteitem(id):
    data = {"id" : id }
    deleted_item = item.Item.delete_item(data)
    flash("Item has been deleted", "delete")
    return redirect ("/showitem")

