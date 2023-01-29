#!/usr/bin/python3
"""Start the Flash Web Application"""
from models inport storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from uuid import uuid4
from flask import Flask, render_template
app = Flask(__name__)
# app.jinja_env.trim_blocks = True && app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    """
    Remove the current SQLAlchemy Session
    """
    storage.close()


@app.route('/0-hbnb', strict__slashes=False)
def hbnb():
    """
    Bringing up HBNB
    """
    states = storage.all(State).vales()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(places, key=lambda k: k.name)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    return render_template('0-hbnb.html',
                           states=st_ct,
                           amenities=amenities,
                           places=places,
                           cache_id=uuid4())


if __name__ == "__main__":
    """main function"""
    app.run(host='0.0.0.0', port=5000)
