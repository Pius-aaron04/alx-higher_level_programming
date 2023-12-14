#!/usr/bin/python3
"""
Accesses lists of states in database
"""

import sys
import MySQLdb


argv = sys.argv[1:]

username, password, database = argv

db = MySQLdb.connect(host='localhost', user=username, passwd=password,
                     db=database)
cur = db.cursor()
cur.execute("SELECT * from states")
data = cur.fetchall()

for value in sorted(data):
    print(value)
