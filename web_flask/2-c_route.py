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


if __name__ == '__main__':
    app.run()
