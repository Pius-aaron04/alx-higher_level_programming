#!/usr/bin/python3
"""
Accesses lists of states in database
"""

import sys
import MySQLdb

if __name__ == '__main__':
    argv = sys.argv[1:]
    username, password, database = argv

    db = MySQLdb.connect(host='localhost', user=username, passwd=password,
                     db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    data = cur.fetchall()

    for value in data:
        print(value)
    cur.close()
    db.close()
