#!/usr/bin/python3

"""
1. A script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":

    """ Extract arguments """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    """ Connect to database """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)

    """ Execute query and fetch results """
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
                 JOIN states\
                 ON cities.state_id = states.id\
                 WHERE states.name=%s\
                 ORDER BY cities.id ASC", (state_name,))
    rows = cur.fetchall()

    """ Display results """
    city_names = [row[0] for row in rows]
    city_list = ', '.join(city_names)
    print(city_list)

    """  Close database connection """
    cur.close()
    db.close()
