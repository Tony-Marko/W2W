from asyncio.windows_events import NULL
from flask_app import app
# from flask_app.models import item
import os, imghdr
from flask import redirect, request, session, flash
from werkzeug.utils import secure_filename
from flask_app.models import item

# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
# app.config['MAX_CONTENT_PATH'] = 2*1024*1024 #2MB

UPLOAD_FOLDER = 'flask_app/static/img/uploads'

app.config['UPLOAD_PATH'] = UPLOAD_FOLDER
app.config['UPLOAD_EXTENSIONS'] = ['pdf', 'png', 'jpg', 'jpeg', 'gif', '.webp']
app.config['MAX_CONTENT_LENGTH'] = 5* 1024 * 1024 #5MB

def validate_image(stream):
    header = stream.read(512)
    stream.seek(0) 
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')

@app.route('/upload', methods=['POST'])
def upload_files():
    uploaded_file = request.files['image']
    filename = secure_filename(uploaded_file.filename)
    # print("$$$$$$$$$$$", request.form)
    x = session['user_id']
    y = request.form['item_id']
    # print("$$$$$$$$$", filename)
    newpage = f'/showitem/{y}'
    if filename != '':
        filename = f'{x}_{y}_{filename}'
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
                file_ext != validate_image(uploaded_file.stream):
            flash("File error", "itemupload")
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        print("Filepath is", os.path.join(app.config['UPLOAD_PATH'], filename))
        filepath = f'img/uploads/{filename}'
        flash("File uploaded", "itemupload")
        data = {
            'id' : y,
            'image' : filepath
        }
        item.Item.edit_image_url(data)
    else:
        flash("No file attached", "itemupload")
        return redirect (newpage)
    return redirect (newpage)

# @app.route('/editupload', methods=['POST']) #experiment for later
# def edit_upload_files():
#     uploaded_file = request.files['image']
#     filename = secure_filename(uploaded_file.filename)
#     # print("$$$$$$$$$$$", request.form)
#     x = session['user_id']
#     y = request.form['item_id']
#     # print("$$$$$$$$$", filename)
#     newpage = f'/edititem/{y}'
#     if filename != '':
#         filename = f'{x}_{y}_{filename}'
#         file_ext = os.path.splitext(filename)[1]
#         if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
#                 file_ext != validate_image(uploaded_file.stream):
#             flash("File error", "itemupload")
#         uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
#         print("Filepath is", os.path.join(app.config['UPLOAD_PATH'], filename))
#         filepath = f'img/uploads/{filename}'
#         flash("File uploaded", "itemupload")
#         data = {
#             'id' : y,
#             'image' : filepath
#         }
#         item.Item.edit_image_url(data)
#     else:
#         flash("No file attached", "itemupload")
#         return redirect (newpage)
#     return redirect (newpage)