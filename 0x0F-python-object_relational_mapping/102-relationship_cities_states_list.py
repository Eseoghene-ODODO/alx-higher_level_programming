#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_101_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == '__main__':
    # Get the MySQL login credentials
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Create the connection engine to the database
    engine = create_engine(f'mysql+mysqldb://{mysql_user}:{mysql_password}\
                             @localhost:3306/{db_name}')

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query all City objects and their associated State objects
    cities = session.query(City).order_by(City.id).all()

    # Print the results
    for city in cities:
        print(f'{city.id}: {city.name} -> {city.state.name}')

    # Close the session
    session.close()
