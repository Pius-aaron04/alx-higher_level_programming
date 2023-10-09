#!/usr/bin/python3
"""
Contains my_list class definition.
"""


class MyList(list):
    """
    A subclass of list class.
    """

    def __init__(self, *args):
        """
        initializes instance.
        """

        super().__init__(*args)

    def print_sorted(self):
        """
        prints instance in sorted ascending order
        """

        new_list = sorted(self)

        print(new_list)
