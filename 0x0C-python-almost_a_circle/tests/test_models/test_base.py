"""
this module contain unit tests
"""

import unittest
from unittest.mock import patch
import io
from models.base import Base


class TestClassBase(unittest.TestCase):
    """
    Unittest for private attribute.
    """

    def setUp(self):
        """
        sets up variables for use.
        """

        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(20)
        self.b4 = Base()

    def test_private_attribute(self):
        """
        test for Base class private attribute.
        """

        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 20)
        self.assertEqual(self.b4.id, 3)
        with self.assertRaises(AttributeError):
            print(self.b4.__nb_objects)
