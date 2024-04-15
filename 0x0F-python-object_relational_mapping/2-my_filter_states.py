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
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}'\
             ORDER BY states.id ASC".format(state_name)
    cur.execute(query)
    rows = cur.fetchall()

    """ Display results """
    for row in rows:
        print(row)

    """  Close database connection """
    cur.close()
    db.close()
