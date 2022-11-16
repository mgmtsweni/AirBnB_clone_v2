#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models import *
app = Flask(__name__)


@app.teardown_appcontext
def tear_down():
    """Remove current SQLAlchemy session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """returns HTML page wit states and id"""
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
