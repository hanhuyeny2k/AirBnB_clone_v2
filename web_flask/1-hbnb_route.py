#!/usr/bin/python3
from flask import Flask
"""
Listening on 0.0.0.0, port 5000, route /hbnb display HBNB
"""
app = Flask(__name__)


@app.route('/')
def home():
    """ return Hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb')
def path_hbnb():
    """ return HBNB """
    return "HBNB"
app.run(host="0.0.0.0", port=5000)
app.route.map(strict_slashes=False)
