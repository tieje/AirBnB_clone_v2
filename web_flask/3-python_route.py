#!/usr/bin/python3
'''An addition that returns just HBNB'''
from typing import Text
from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello, HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''An addition that returns just HBNB'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def displayText(text):
    '''Displays the text variable'''
    return f'C {escape(text)}'


@app.route("/python", strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def displayPythonText(text='is cool'):
    '''Displays the text variable but with python'''
    display_text = escape(text).replace('_', ' ')
    return f'Python {display_text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
