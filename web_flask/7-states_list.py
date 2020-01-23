#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
"""
Start Flask web app, listening on 0.0.0.0, port 5000, display Hello HBNB!
"""


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close(self):
    storage.close()

@app.route('/states_list')
def HTML_States(states=None):
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
