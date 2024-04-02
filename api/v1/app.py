#!/usr/bin/python3
"""code to start the api"""

from os import getenv
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

if __name__ == "__main__":
    app.run(getenv("HBNB_API_HOST"), getenv("HBNB_API_PORT"))
