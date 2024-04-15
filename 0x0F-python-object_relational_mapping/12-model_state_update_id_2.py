#!/usr/bin/python3
"""
changes the name of a State object from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    """Create a new Engine instance"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    """Create a configured SessionFactory"""
    Session = sessionmaker(bind=engine)

    """Create a new session"""
    session = Session()

    """Query the database"""
    state = session.query(State).filter_by(id=2).first()

    """Check if the state exists"""
    if state:
        state.name = "New Mexico"
        session.commit()
    else:
        print("Not found")

    """Close the session"""
    session.close()
