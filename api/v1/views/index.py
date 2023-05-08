#!/usr/bin/python3
"""
Index page of the server
"""

from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def status():
    """Returns the status

    Returns:
        JSON: Status in JSON Format 
    """
    return jsonify({'status': 'OK'})
