#!/usr/bin/python3
"""
Start Flask web app, listening on 0.0.0.0, port 5000, display Hello HBNB!
"""
from flask import Flask, render_template
from models import storage
from models.city import City
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close(self):
    """ close storage """
    storage.close()


@app.route('/cities_by_states')
def cities_by_states():
    """ fetch data from the storage engine"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
