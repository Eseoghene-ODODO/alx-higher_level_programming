#!/usr/bin/python3
"""
Script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """ Create connection"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    search_state = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name),
                           pool_pre_ping=True)

    """ Create session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """ Query database"""
    query = session.query(State).filter(State.name == search_state).first()

    """ Display result"""
    if query:
        print(query.id)
    else:
        print("Not found")
