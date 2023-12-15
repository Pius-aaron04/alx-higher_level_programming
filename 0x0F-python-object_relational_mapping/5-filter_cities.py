#!/usr/bin/python3
"""
List all cities in specified state.
"""
import sys
import MySQLdb


def main():
    """
    main function for the queries.
    """

    username, password, database, state_name = sys.argv[1:]
    db = MySQLdb.connect(host='localhost', user=username, passwd=password,
                         db=database,  port=3306)
    cur = db.cursor()
    squery = """SELECT cities.name FROM cities
    JOIN states on cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC;"""
    cur.execute(squery, (state_name,))

    rows = cur.fetchall()

    for i, row in enumerate(rows):
        if i != len(rows) - 1:
            print(row[0], end=", ")
        else:
            print(row[0])


if __name__ == '__main__':
    main()
