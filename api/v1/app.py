#!/usr/bin/python3
"--"

from flask import Flask
from models import storage
from api.v1.views import app_views


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """--"""
    storage.close()
