#!/usr/bin/python3
"""list of states"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def close(error):
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def hbnb():
    """filters"""
    states = storage.all('State')
    amenities = storage.all('Amenities')
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
