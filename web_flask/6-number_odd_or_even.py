#!/usr/bin/python3
from flask import Flask
from flask import render_template
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


@app.route('/number_template/<int:n>')
def HTML_only(n=None):
    """ display HTML page only if n in an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def even_odd(n=None, m=None):
    """ display n is even or odd in HTML page"""
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', n=n, m='is even')
    else:
        return render_template('6-number_odd_or_even.html', n=n, m='is odd')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
