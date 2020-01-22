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


@app.route('/python/<text>')
@app.route('/python/')
@app.route('/python')
def python_is(text='is cool'):
    """ return Python is cool by default """
    if text:
        new_text = text.replace("_", " ")
        return 'Python {}'.format(new_text)


@app.route('/number/<int:n>')
def int_only(n):
    """ display 'n is a number' only if n is an integer"""
    return '{} is a number'.format(n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
