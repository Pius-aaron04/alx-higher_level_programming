#!/usr/bin/python3
"""
This module contains unittest test cases for the max function.
"""

import unittest


max_integer = __import__('6-max_integer').max_integer


class TestMax(unittest.TestCase):
    """
    A sub class for test cases.
    """

    def test_max_integer(self):
        """
        this function test for the max_integer function.
        """

        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 2, 4]), 4)
        self.assertEqual(max_integer([-4, 100, 8, -10]), 100)
        self.assertEqual(max_integer([91, 8, 0, 1]), 91)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([3, 0, 55, 9, 65, 89, 1000]), 1000)
        self.assertEqual(max_integer([1]), 1)
