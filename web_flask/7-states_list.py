#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models import *
app = Flask(__name__)


@app.teardown_appcontext
def tear_down(self):
    """Remove current SQLAlchemy session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list(states):
    """display a HTML page with the states"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    """Main Function"""
    app.run(host='0.0.0.0', port=5000, debug=True)
