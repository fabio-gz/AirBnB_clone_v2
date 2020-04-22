#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, escape, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """prints  hello"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """prints HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def variables(text):
    """print variable"""
    return 'C {}'.format(escape(text).replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_var(text='is cool'):
    """print var"""
    return 'Python {}'.format(escape(text).replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """print number"""
    return '{} is a number'.format(escape(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def template(n):
    """print template"""
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
