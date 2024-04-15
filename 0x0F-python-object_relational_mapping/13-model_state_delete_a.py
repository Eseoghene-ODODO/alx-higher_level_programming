#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == '__main__':
    """Set up the connection to the database"""
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_db = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(mysql_user, mysql_password, mysql_db),
                           pool_pre_ping=True)

    """Create a session to communicate with the database"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """Query and delete all State objects containing letter a in their name"""
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_with_a:
        session.delete(state)
    session.commit()

    """Close the session"""
    session.close()
