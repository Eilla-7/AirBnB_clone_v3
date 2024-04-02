#!/usr/bin/python3
"""code to start the api"""

from os import getenv
from flask import Flask
from models import storage
from api.v1.views import app_views


app = Flask(__name__)

if __name__ == "__main__":
    app.run(getenv("HBNB_API_HOST"), getenv("HBNB_API_PORT"))
