#!/usr/bin/python3
"""
Accesses lists of states in database
"""

import sys
import MySQLdb

def main():
    username, password, database, state_name = sys.argv[1:]

    db = MySQLdb.connect(host='localhost', user=username, passwd=password,
                         db=database, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s", (state_name,))
    data = cur.fetchall()

    for value in sorted(data):
        print(value)
    cur.close()
    db.close()

if __name__ == '__main__':
    main()
