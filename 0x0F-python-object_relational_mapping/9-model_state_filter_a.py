#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter
a from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    """ Script should take 3 arguments: mysql username,
        mysql password and database name"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    """ Connect to a MySQL server running on localhost at port 3306"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))

    """ Create a configured "Session" class"""
    Session = sessionmaker(bind=engine)

    """ Create a Session instance"""
    session = Session()

    """ Get all State objects that contain the letter a"""
    states = (session.query(State).filter(State.name.like('%a%'))
              .order_by(State.id).all())

    """ Display results"""
    for state in states:
        print("{}: {}".format(state.id, state.name))
