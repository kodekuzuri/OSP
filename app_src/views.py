from app_src import app
from flask import render_template, jsonify, make_response, send_file, request, redirect
from osp import Item

@app.route("/")
def index():
    return render_template("Signin Template .html")




## this returns the file as a download :(
@app.route('/testitem') 
def index1():
    item = Item.objects().first()
    return send_file(item.photo, as_attachment=True, attachment_filename='myfile.jpeg')