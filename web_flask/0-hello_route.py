#!/usr/bin/python3
from flask import Flask
"""
Start Flask web app, listening on 0.0.0.0, port 5000, display Hello HBNB!
"""
if __name__ == "__main__":
    app = Flask(__name__)


@app.route('/')
def home():
    """ return Hellow HBNB """
    return "Hello HBNB!"
app.run(host="0.0.0.0", port=5000)
app.route.map(strict_slashes=False)
