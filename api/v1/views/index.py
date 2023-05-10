#!/usr/bin/python3
"""
Index page of the server

Routes:
    /status: Get status of the server
    /stas: Get the number of each object by type
"""

from flask import jsonify
import api.v1.views as apv
# from api.v1.views import app_views
import models as m
# from models import storage


if __name__ == "__main__":
    @apv.app_views.route('/status', methods=['GET'], strict_slashes=False)
    def status():
        """Returns the status

        Returns:
            JSON: Status in JSON Format
        """
        return jsonify({'status': 'OK'})


    @apv.app_views.route('/stats', methods=['GET'], strict_slashes=False)
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
            objects[value] = m.storage.count(key)
        return jsonify(objects)
