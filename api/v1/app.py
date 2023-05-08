#!/usr/bin/python3
"""
Check for the status of the API

Route:
    /api/v1/status
"""

from flask import Flask
from models import storage
from api.v1.views import app_views
import os


app = Flask(__name__)

# Register Blueprint
app.register_blueprint(app_views)

# Server environment
host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = os.getenv('HBNB_API_PORT', 5000)


@app.teardown_appcontext
def teardown(exception=None):
    """
    Teardown
    """
    storage.close()


if __name__ == "__main__":
    app.run(host=host, port=port, threaded=True)