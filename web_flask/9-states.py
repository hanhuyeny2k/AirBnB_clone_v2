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


@app.route('/states')
@app.route('/states/<id>')
def state_by_id(id=None):
    """ fetch data from the storage engine"""
    states = storage.all(State)
    if id is not None:
        key = 'State.' + id
    else:
        key = None
    return render_template('9-states.html', key=key, states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
