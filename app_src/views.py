from flask.helpers import make_response
from flask import request, redirect
from app_src import app
from flask import render_template, jsonify, make_response, send_file
import json
import random
import gmaps
import gmplot
from statistics import mean
import os


@app.route("/")
def index():
    return render_template("Signin Template .html")


