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


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """display a HTML page like 6-index.html from static"""
    states = storage.all("State").values()
    filters = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states,
                           filters=filters)


if __name__ == '__main__':
    """Main Function"""
    app.run(host='0.0.0.0', port=5000, debug=True)
