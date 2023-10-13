"""
this module contain unit tests
"""

import unittest
import models.base as base
from models.rectangle import Rectangle


class TestClassBase(unittest.TestCase):
    """
    Unittest for private attribute.
    """

    def setUp(self):
        """
        sets up variables for use.
        """

        self.b1 = base.Base()
        self.b2 = base.Base()
        self.b3 = base.Base(20)
        self.b4 = base.Base()

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


class TestClassRectangle(unittest.TestCase):
    """
    tests the rectangle class.
    """

    def setUp(self):
        """
        sets up variables for use.
        """

        self.r1 = Rectangle(2, 5)

    def test_rectangle_attr(self):
        """
        tests rectangle instance attributes.
        """

        with self.assertRaises(TypeError):
            rect = Rectangle("2", 5)
        with self.assertRaises(TypeError):
            rect1 = Rectangle(3, "3")
        with self.assertRaises(TypeError):
            rect = Rectangle([1, 3], (1, 2, 3))
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 4, "2")
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, 2, [5])
