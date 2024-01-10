#!/usr/bin/python3
"""
Gets GitHub user id via GitHub API using the user name and password
as authentication
"""

import requests
import sys


def main():
    """ main function """
    user_name = sys.argv[1]
    password = sys.argv[2]

    r = requests.get('https://api.github.com/user', auth=(user_name, password))
    data = r.json()
    if 'id' in data.keys():
        print(data['id'])
    else:
        print('None')


if __name__ == '__main__':
    main()
