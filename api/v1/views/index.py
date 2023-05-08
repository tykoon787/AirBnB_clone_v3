#!/usr/bin/python3
"""
Index page of the server

Routes:
    /status: Get status of the server
    /stas: Get the number of each object by type
"""

from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Returns the status

    Returns:
        JSON: Status in JSON Format
    """
    return jsonify({'status': 'OK'})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """Returns the count of all class objects"""
    objects: dict = {}
    classes: dict = {
        "Amenity": "amenities",
        "City": "cities",
        "Place": "places",
        "Review": "reviews",
        "State": "states",
        "User": "users"
    }
    for key, value in classes.items():
        objects[value] = storage.count(key)
    return jsonify(objects)
