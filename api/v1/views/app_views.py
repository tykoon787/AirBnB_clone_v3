#!/usr/bin/python3
from flask import Blueprint
from api.v1.views.index import *
# TODO: Create a file index.py:
#   1) import app_views from api.v1.views
#   2) Create a route /status on the object app_vies that returns a JSON: "status":"ok"

app_views = Blueprint('app_views', __name__, url_prefix="/api/v1")
