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


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """display the states and cities"""
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


if __name__ == '__main__':
    """Main Function"""
    app.run(host='0.0.0.0', port=5000, debug=True)
