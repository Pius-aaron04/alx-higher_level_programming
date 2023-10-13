"""
contains test case for rectangle class
"""

import unittest
from unittest.mock import patch
import io
from models import rectangle

Rectangle = rectangle.Rectangle


class TestClassRectangle(unittest.TestCase):
    """
    tests the rectangle class.
    """

    def test_rectangle_inst_constr(self):
        """
        tests rectangle instance creation with invalid
        types
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
        with self.assertRaises(ValueError):
            rect = Rectangle(-2, 5)

    def test_rectangle_attr_get(self):
        """
        test rectangle atrribute value with the
        get method.
        """

        r1 = Rectangle(2, 5)
        r2 = Rectangle(3, 9, 1, 2)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.y, 2)
        with self.assertRaises(AttributeError):
            r2.__nb_objects

    def test_rectangle_atrr_set(self):
        """
        tests setting rectangle attributes.
        """

        r1 = Rectangle(2, 5)
        r2 = Rectangle(3, 9, 1, 2)
        r3 = Rectangle(2, 3)
        r1.x = 10
        self.assertEqual(r1.x, 10)
        r1.y = 5
        self.assertEqual(r1.y, 5)
        r1.width = 10
        self.assertEqual(r1.width, 10)
        r1.height = 20
        self.assertEqual(r1.height, 20)
        r3.y = 8
        self.assertEqual(r3.y, 8)
        r1.x = 0
        self.assertEqual(r1.x, 0)
        r1.y = 0
        self.assertEqual(r1.y, 0)

    def test_rectangle_attr_set_invalid(self):
        """
        tests for invalid seeting of attributes values.
        """

        r1 = Rectangle(2, 5)
        r2 = Rectangle(3, 9, 1, 2)
        r3 = Rectangle(2, 3)
        with self.assertRaises(TypeError):
            r2.width = "10"
        with self.assertRaises(TypeError):
            r3.height = (1, 2)
        with self.assertRaises(TypeError):
            r3.x = {1: 0}
        with self.assertRaises(TypeError):
            r3.width = 0.5

    def test_rectangle_area_attr(self):
        """
        tests rectangle instance attribute.
        """

        r1 = Rectangle(2, 5)
        r2 = Rectangle(3, 9, 1, 2)
        r3 = Rectangle(2, 3)
        self.assertEqual(r1.area(), 10)
        self.assertEqual(r2.area(), 27)
        self.assertEqual(r3.area(), 6)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_output_without_x_y(self, mock_stdout):
        """
        test the display of rectangle instance attribute.
        """

        rect = Rectangle(3, 3)
        rect.display()
        captured_output = mock_stdout.getvalue()
        self.assertEqual(captured_output, "###\n###\n###\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_non_equal_sides(self, mock_stdout):
        """
        test display for non equal sides.
        """

        rect = Rectangle(5, 3)
        rect.display()
        captured_output = mock_stdout.getvalue()
        self.assertEqual(captured_output, "#####\n#####\n#####\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_non_equal_sides1(self, mock_stdout):
        """
        test display for non equal sides.
        """

        rect = Rectangle(4, 5)
        rect.display()
        captured_output = mock_stdout.getvalue()
        self.assertEqual(captured_output, "####\n####\n####\n" +
                         "####\n####\n")

    def test_instance_ids(self):
        """
        tests instances ids
        """

        rect1 = Rectangle(2, 5)
        rect2 = Rectangle(3, 10)
        rect3 = Rectangle(5, 2, id=5)
        rect4 = Rectangle(3, 2, 3, 4)

        self.assertEqual(rect1.id, 1)
        self.assertEqual(rect2.id, 2)
        self.assertEqual(rect3.id, 5)
        self.assertEqual(rect4.id, 3)

    def test_for_rectangle_string_rep(self):
        """
        test for string representation of rectangle instance.
        """

        rec = Rectangle(10, 15, 0, 9, 20)
        self.assertEqual(str(rec), "[Rectangle] (20) 0/9 - 10/15")

        rec2 = Rectangle(2, 4, id=9)
        self.assertEqual(str(rec2), "[Rectangle] (9) 0/0 - 2/4")
        self.assertEqual(rec2.__str__(), "[Rectangle] (9) 0/0 - 2/4")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_printed_inst_rep(self, mock_stdout):
        """
        test printable instance string representation.
        """

        rec = Rectangle(10, 15, 0, 9, 20)
        print(rec)

        captured = mock_stdout.getvalue()
        self.assertEqual(captured, '[Rectangle] (20) 0/9 - 10/15\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_rectangle_display_with_x_y(self, mock_stdout):
        """
        tests for rectangle instance printing with x, y
        adjustment handled.
        """

        rect = Rectangle(2, 3, 1, 2, 14)
        rect.display()

        captured = mock_stdout.getvalue()

        self.assertEqual(captured, "\n\n  ##\n" +
                         "  ##\n  ##\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_rectangle_display_with_x_y1(self, mock_stdout):
        """
        tests for rectangle instance printing with x, y
        adjustment handled.
        """

        rect = Rectangle(3, 3, 1, 2, 14)
        rect.display()

        captured = mock_stdout.getvalue()

        self.assertEqual(captured, "\n\n ###\n" +
                         " ###\n ###\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_rectangle_display_with_x_y_2(self, mock_stdout):
        """
        tests for rectangle instance printing with x, y
        adjustment handled with x, y with default value.
        """

        rect = Rectangle(5, 8)
        rect.display()

        captured = mock_stdout.getvalue()

        self.assertEqual(captured, "#####\n#####\n#####\n#####\n#####\n#####\n"
                         "#####\n#####\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_rectangle_display_with_x_y3(self, mock_stdout):
        """
        tests for rectangle instance printing with x, y
        adjustment handled. with x set and y not set
        """

        rect = Rectangle(2, 3, 1)
        rect.display()

        captured = mock_stdout.getvalue()

        self.assertEqual(captured, " ##\n" +
                         " ##\n ##\n")
 
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_rectangle_display_with_x_y(self, mock_stdout):
        """
        tests for rectangle instance printing with x, y
        adjustment handled, with x not setted and y setted
        """

        rect = Rectangle(2, 3, y=3)
        rect.display()

        captured = mock_stdout.getvalue()

        self.assertEqual(captured, "\n\n\n##\n" +
                         "##\n##\n")
