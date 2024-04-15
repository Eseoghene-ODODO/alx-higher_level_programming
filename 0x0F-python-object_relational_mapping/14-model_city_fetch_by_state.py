#!/usr/bin/python3
""" Script that prints all City objects from the database hbtn_0e_14_usa """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == '__main__':
    """Connection settings"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    connection = 'mysql+mysqldb://{}:{}@localhost:3306/{}'

    """Create engine and bind Base to it"""
    engine = create_engine(connection.format(username, password, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    """Create session and query for all cities"""
    session = Session()
    cities = session.query(City, State).join(State).order_by(City.id).all()
    """Print cities grouped by state"""
    for city, state in cities:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    """Close session"""
    session.close()
