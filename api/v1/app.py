#!/usr/bin/python3
"""
Check for the status of the API

Route:
    /api/v1/status
"""

from flask import Flask
from models import storage
from api.v1.views import app_views
# TODO: Register blueprint app_views to flask Instance app

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown():
    """
    Teardown
    """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)
