from app_src import app
from flask import render_template, jsonify, make_response, send_file, request, redirect


@app.route("/")
def index():
    return render_template("Signin Template .html")


