#!/usr/bin/python3
'''An addition that returns just HBNB'''
from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def numberdisplay(n):
    '''Displays the number'''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:number>', strict_slashes=False)
def displaytemplate(number):
    '''Displays a template'''
    return render_template('5-number.html', number=number)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def EvenOrOdd(n):
    '''Displays a template'''
    if n % 2 == 1:
        return render_template('6-number_odd_or_even.html', number=n, EvenOrOdd='odd')
    return render_template('6-number_odd_or_even.html', number=n, EvenOrOdd='even')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
