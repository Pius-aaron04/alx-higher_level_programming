#!/usr/bin/python3
"""
List all statesin cities table.
"""
import sys
import MySQLdb


def main():
    username, password, database = sys.argv[1:]
    db = MySQLdb.connect(host='localhost', user=username, passwd=password,
                         db=database,  port=3306)
    cur = db.cursor()
    cur.execute('SELECT * FROM cities ORDER BY cities.id ASC')

    rows = cur.fetchall()

    for row in rows:
        print(row)


if __name__ == '__main__':
    main()
