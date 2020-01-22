#!/usr/bin/python3
from flask import Flask
"""
Listening on 0.0.0.0, port 5000, route /c/<text>
"""
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def home():
    """ return Hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb')
def path_hbnb():
    """ return HBNB """
    return "HBNB"


@app.route('/c/<text>')
def C_is(text):
    """ return C <text> """
    new_text = text.replace("_", " ")
    return 'C {}'.format(new_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
