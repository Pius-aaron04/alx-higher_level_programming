#!/usr/bin/python3
"""
Accesses lists of states in database
"""

import sys
import MySQLdb


argv = sys.argv[1:]

username, password, database = argv

db = MySQLdb.connect(host='localhost', user=username, passwd=password,
                     db=database, port=3306)
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY id")
data = cur.fetchall()

for value in data:
    if value[1].startswith('N'):
        print(value)
cur.close()
db.close()
