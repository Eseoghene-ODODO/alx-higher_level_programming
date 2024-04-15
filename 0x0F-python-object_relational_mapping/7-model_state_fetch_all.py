#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    """ Create a new Engine instance"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    """ Create all tables stored in this metadata."""
    Base.metadata.create_all(engine)

    """ Create a new Session instance"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """ Query all State objects ordered by id and print them"""
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

    """ Close the session"""
    session.close()
