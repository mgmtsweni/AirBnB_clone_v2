#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """Function that displays Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_world():
    """Function that returns a printed message"""
    return 'HBNB!'


@app.route('c/<text>', strict_slashes=False)
def hello_world():
    """Function that returns a printed message"""
    return 'C ' + text.replace('_', ' ')


@app.route('python', strict_slashes=False)
@app.route('python/<text>', strict_slashes=False)
def hello_world(text='is cool'):
    """Function that returns a printed message"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<n>', strict_slashes=False)
def hello_world():
    """Function that returns a printed message"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<n>', strict_slashes=False)
def hello_world():
    """Function that returns a printed message"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def hello_world():
    """display a HTML page only if n is an integer"""
    e_o = "event" if (n % 2 == 0) else "odd"
    return render_template('6-number_odd_or_even.html', n=n, e_o=e_o)


if __name__ == '__main__':
    """Main Function"""
    app.run(host='0.0.0.0', port=5000, debug=True)
