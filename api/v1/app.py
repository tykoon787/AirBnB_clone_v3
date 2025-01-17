#!/usr/bin/python3
"""
Serves the flask application
"""

from flask import Flask, jsonify
import models as m
# from models import storage
import os
import api.v1.views as apv
# from api.v1.views import app_views

app = Flask(__name__)

# Blueprint of app_views
app.register_blueprint(apv.app_views)


# Server environment config
host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = os.getenv('HBNG-API_PORT', 5000)


@app.teardown_appcontext
def teardown(exception=None):
    """Teardown for app"""
    m.storage.close()


@app.errorhandler(404)
def not_found(error):
    """Handle 404, not found"""
    return jsonify({'error': 'Not Found'}), 404


if __name__ == "__main__":
    """
    Run server
    """
    app.run(host=host, port=port, threaded=True)
