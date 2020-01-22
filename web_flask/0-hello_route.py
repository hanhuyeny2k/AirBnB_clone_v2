#!/usr/bin/python3
from flask import Flask
"""
Start Flask web app, listening on 0.0.0.0, port 5000, display Hello HBNB!
"""


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def home():
    """ return Hellow HBNB """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
