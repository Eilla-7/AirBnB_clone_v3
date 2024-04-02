#!/usr/bin/python3
"""code to start the api"""

import os
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

#register blueprint
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(exception):
    """ tear down function"""
    storage.close()

@app.errorhandler(404)
def handle_error_404(error):
    """ handle not found error 404"""
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
