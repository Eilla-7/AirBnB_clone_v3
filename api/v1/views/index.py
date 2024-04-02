#!/usr/bin/python3
"""index.py"""

from flask import jsonify
from api.v1.views import app_views

@app_views.route("/status", methods=['GET'], strict_slashes=False)
def status():
    """ return the status ok"""
    return jsonify({"status": "OK"})
