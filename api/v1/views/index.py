#!/usr/bin/python3
"""
Index page of the application

Returns:
    JSON : Status of the server
"""

from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'])
def get_status():
    """
    Function to get the status
    """
    return jsonify({'status': 'OK'})
