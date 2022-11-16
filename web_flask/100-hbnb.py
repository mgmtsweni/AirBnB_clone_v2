#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
app = Flask(__name__)

@app.teardown_appcontext
def teardown(self):
    """Tear down"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb_():
    """Displays hbnb filters HTML template """
    d_state = storage.all(State).value()
    d_city = storage.all(City).value()
    d_amenity = storage.all(Amenity).value()
    d_place = storage.all(Place).value()

    return render_template('100-hbnb.html',d_state=d_state, d_city=d_city,
                           d_amenity=d_amenity, d_place=d_place)

if __name__ == '__main__':
    """Main Function"""
    app.run(host='0.0.0.0')
