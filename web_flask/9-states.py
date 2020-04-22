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
def states_alone():
    """states"""
    states = storage.all('State')
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """states id"""
    states = storage.all('State')
    return render_template('9-states.html', states=states, id=id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
