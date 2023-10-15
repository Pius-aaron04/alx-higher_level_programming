"""
Test cases for Square Classes.
"""

import unittest
import models.square
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """
    Test class for Square instances/class
    """

    def test_instanciation(self):
        """
        test for instance instantiation.
        """

        s1 = Square(3)
        self.assertEqual(s1.size, 3)
        
    def test_update(self):
        """
        test update method.
        """

        s2 = Square(3)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            s2.update(id=2, width='5')
