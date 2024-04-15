#!/usr/bin/python3

"""
1. A script that lists all states from the database hbtn_0e_0_usa:
2. Your script should take 3 arguments: mysql username, mysql password and
database name(no argument validation needed)
3. You must use the module MySQLdb (import MySQLdb)
"""

import MySQLdb
import sys

if __name__ == "__main__":

    """ Extract arguments """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    """ Connect to database """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)

    """ Execute query and fetch results """
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY\
                'N%' ORDER BY states.id ASC")
    rows = cur.fetchall()

    """ Display results """
    for row in rows:
        print(row)

    """  Close database connection """
    cur.close()
    db.close()
