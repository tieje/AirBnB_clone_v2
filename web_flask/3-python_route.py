#!/usr/bin/python3
'''An addition that returns just HBNB'''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''An addition that returns just HBNB'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    '''Displays the text variable'''
    text = text.replace("_", " ")
    return 'C {}'.format(text)


@app.route("/python", strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def displayPythonText(text='is cool'):
    '''Displays the text variable but with python'''
    display_text = text.replace('_', ' ')
    return 'Python {}'.format(display_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
