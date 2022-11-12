#!/usr/bin/python3
"""A script that starts a Flask web application"""


from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_world():
    """Function that returns a printed message"""
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
    """display “Python” followed by the value of the text"""
    return 'Python ' + text.replace('_', ' ')

if __name__=='__main__':
    """Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)
