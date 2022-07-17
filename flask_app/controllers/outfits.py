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


@app.route("/addnewoutfit", methods=['post'])
def addnewoutfit():
    new_outfit = outfit.Outfit.addnewoutfit(request.form)
    pageid = new_outfit
    newpage = f'/myoutfit/{pageid}'
    return redirect (newpage)

#Result from first outfit saved
# Running Query: INSERT INTO outfits (headwear, top, waist, bottom, footwear, acc1, acc2, user_id)
#                 VALUES ('3', '13', '14', '18', '22', '26', '0', '1');
# Result is 1

@app.route("/editoutfit/<id>")
def editoutfit(id):
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
    data = {"id" : id }
    gotoutfit = outfit.Outfit.get_outfit_by_id(data)
    headwear = item.Item.get_item_for_outfit(gotoutfit.headwear)
    top = item.Item.get_item_for_outfit(gotoutfit.top)
    waist = item.Item.get_item_for_outfit(gotoutfit.waist)
    bottom = item.Item.get_item_for_outfit(gotoutfit.bottom)
    footwear = item.Item.get_item_for_outfit(gotoutfit.footwear)
    acc1 = item.Item.get_item_for_outfit(gotoutfit.acc1)
    acc2 = item.Item.get_item_for_outfit(gotoutfit.acc2)
    return render_template ("editoutfit.html", gotoutfit = gotoutfit, headwear =headwear, top = top, waist = waist, bottom = bottom, footwear = footwear, acc1 = acc1, acc2 =acc2, all_headwear = all_headwear, all_top=all_top, all_waist= all_waist, all_bottom = all_bottom, all_footwear = all_footwear, all_accessory = all_accessory)

# ////////UPDATE///////////
@app.route("/editthisoutfit", methods = ['post'])
def editthisoutfit():
    print(request.form)
    data = request.form
    edited_outfit = outfit.Outfit.editoutfit(data)
    pageid = request.form['id']
    print("$$$$$$$$$$$$$ Pagieid =", pageid)
    newpage = f'/myoutfit/{pageid}'
    return redirect (newpage)
    #note this does not include images, images removed from parsed data

# # ////////DELETE///////////
# # note: add flash messages to confirm deletions
@app.route("/deleteoutfit/<id>")
def deleteoutfit(id):
    data = {"id" : id }
    deleted_outfit = outfit.Outfit.delete_outfit(data)
    return redirect ("/myoutfits")



