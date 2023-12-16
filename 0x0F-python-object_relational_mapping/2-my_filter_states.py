#!/usr/bin/python3
"""
Accesses lists of states in database
"""

import sys
import MySQLdb

if __name__ == '__main__':
    username, password, database, state_name = sys.argv[1:]

    db = MySQLdb.connect(host='localhost', user=username, passwd=password,
                         db=database, port=3306)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name='{}' ORDER BY id"
    cur.execute(query.format(state_name))
    data = cur.fetchall()

    for value in sorted(data):
        print(value)
    cur.close()
    db.close()
