#!/usr/bin/python3
"""
A script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


if __name__ == '__main__':
    """ Defining Aguments"""
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    """Connecting to db"""
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            password=password,
            db=db_name
            )

    """Execute query and fatch results"""
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY\
                'N%' ORDER BY states.id ASC")

    """Display results"""
    for row in rows:
        print(row)

    """Close db connection"""
    cur.close()
    db.close()
