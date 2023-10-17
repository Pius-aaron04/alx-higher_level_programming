"""
Test cases for Square Classes.
"""

import unittest
from unittest.mock import patch
import io
import models.square
from models.square import Square
import os


class TestSquareClass(unittest.TestCase):
    """
    Test class for Square instances/class
    """

    def setUp(self):

        self.s1 = Square(4)
        self.s2 = Square(5, 2, 4)
        self.s3 = Square(10, 0, 9, 9)

    def test_instanciation(self):
        """
        test for instance instantiation.
        """

        self.assertEqual(self.s1.size, 4)
        self.assertEqual(self.s1.x, 0)

    def test_update(self):
        """
        test update method.
        """

        s2 = Square(3)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            s2.update(id=2, width='5')

    def test_rectangle_inst_constr(self):
        """
        tests rectangle instance creation with invalid
        types
        """

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            rect = Square("2", 5)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            rect = Square([1, 3], (1, 2, 3))
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            rect = Square(1, "2")
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            rect = Square(2, 2, [5])
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            rect = Square(-2, 5)

    def test_square_inst_constr_val(self):
        """
        test Square instances for value Errors.
        """

        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r = Square(-2, 5)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r = Square(0, 5)
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            r = Square(2, -5)
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            r = Square(2, -45, 4)
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            r = Square(2, 4, -7)

    def test_square_attr_get(self):
        """
        test Square atrribute value with the
        get method.
        """

        self.assertEqual(self.s1.size, 4)
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s2.x, 2)
        self.assertEqual(self.s2.y, 4)
        self.assertEqual(self.s2.size, 5)
        self.assertEqual(self.s3.id, 9)
        with self.assertRaises(AttributeError):
            self.s1.__nb_objects

    def test_square_atrr_set(self):
        """
        tests setting rectangle attributes.
        """

        self.s1.x = 10
        self.assertEqual(self.s1.x, 10)
        self.s1.y = 5
        self.assertEqual(self.s1.y, 5)
        self.s1.width = 10
        self.assertEqual(self.s1.width, 10)
        self.s1.height = 20
        self.assertEqual(self.s1.height, 20)
        self.s3.y = 8
        self.assertEqual(self.s3.y, 8)
        self.s1.x = 0
        self.assertEqual(self.s1.x, 0)
        self.s1.y = 0
        self.assertEqual(self.s1.y, 0)

    def test_rectangle_attr_set_invalid(self):
        """
        tests for invalid seeting of attributes values.
        """

        with self.assertRaises(TypeError):
            self.s2.size = "10"
        with self.assertRaises(TypeError):
            self.s3.size = (1, 2)
        with self.assertRaises(TypeError):
            self.s3.x = {1: 0}
        with self.assertRaises(TypeError):
            self.s3.y = 0.5

    def test_rectangle_area_attr(self):
        """
        tests rectangle instance attribute.
        """

        r2 = Square(3, 9, 1, 2)
        self.s3 = Square(2, 3)
        self.assertEqual(self.s1.area(), 16)
        self.assertEqual(r2.area(), 9)
        self.assertEqual(self.s3.area(), 4)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_output_without_x_y(self, mock_stdout):
        """
        test the display of rectangle instance attribute.
        """

        rect = Square(3)
        rect.display()
        captured_output = mock_stdout.getvalue()
        self.assertEqual(captured_output, "###\n###\n###\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_non_equal_sides(self, mock_stdout):
        """
        test display for non equal sides.
        """

        rect = Square(5)
        rect.display()
        captured_output = mock_stdout.getvalue()
        self.assertEqual(captured_output, "#####\n#####\n#####\n#####" +
                         "\n#####\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_non_equal_sides1(self, mock_stdout):
        """
        test display for non equal sides.
        """

        rect = Square(4, 5)
        rect.display()
        captured_output = mock_stdout.getvalue()
        self.assertEqual(captured_output, "     ####\n     ####\n     " +
                         "####\n     ####\n")

    def test_instance_ids(self):
        """
        tests instances ids
        """

        rect1 = Square(2, 5)
        rect2 = Square(3, 10)
        rect3 = Square(5, 2, id=5)
        rect4 = Square(3, 2, 3, 4)

        self.assertEqual(rect3.id, 5)
        self.assertEqual(rect4.id, 4)

    def test_for_rectangle_string_rep(self):
        """
        test for string representation of rectangle instance.
        """

        rec = Square(10, 0, 9, 20)
        self.assertEqual(str(rec), "[Square] (20) 0/9 - 10")

        rec2 = Square(2, 4, id=9)
        self.assertEqual(str(rec2), "[Square] (9) 4/0 - 2")
        self.assertEqual(rec2.__str__(), "[Square] (9) 4/0 - 2")
        rec2.update(x=0, y=0)
        self.assertEqual(rec2.__str__(), "[Square] (9) 0/0 - 2")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_printed_inst_rep(self, mock_stdout):
        """
        test printable instance string representation.
        """

        rec = Square(10, 15, 0, 9)
        print(rec)

        captured = mock_stdout.getvalue()
        self.assertEqual(captured, '[Square] (9) 15/0 - 10\n')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_rectangle_display_with_x_y(self, mock_stdout):
        """
        tests for rectangle instance printing with x, y
        adjustment handled.
        """

        rect = Square(2, 1, 2, 14)
        rect.display()

        captured = mock_stdout.getvalue()

        self.assertEqual(captured, "\n\n  ##\n" +
                         "  ##\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_rectangle_display_with_x_y1(self, mock_stdout):
        """
        tests for rectangle instance printing with x, y
        adjustment handled.
        """

        rect = Square(3, 1, 2, 14)
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

        rect = Square(5)
        rect.display()

        captured = mock_stdout.getvalue()

        self.assertEqual(captured, "#####\n#####\n#####\n#####\n#####\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_rectangle_display_with_x_y_3(self, mock_stdout):
        """
        tests for rectangle instance printing with x, y
        adjustment handled with x, y with default value.
        """

        rect = Square(1, 0, 0)
        rect.display()

        captured = mock_stdout.getvalue()

        self.assertEqual(captured, "#\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_rectangle_display_with_x_y3(self, mock_stdout):
        """
        tests for rectangle instance printing with x, y
        adjustment handled. with x set and y not set
        """

        rect = Square(2, 3, 1)
        rect.display()

        captured = mock_stdout.getvalue()

        self.assertEqual(captured, "\n   ##\n   ##\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_rectangle_display_with_x_y(self, mock_stdout):
        """
        tests for rectangle instance printing with x, y
        adjustment handled, with x not setted and y setted
        """

        rect = Square(2, 3, y=3)
        rect.display()

        captured = mock_stdout.getvalue()

        self.assertEqual(captured, "\n\n\n   ##\n" +
                         "   ##\n")

    def test_rectangle_update_method(self):
        """
        tests the update method.
        """

        rect = Square(2, 7, 8, 89)
        rect.update(3)
        self.assertEqual(rect.id, 3)
        rect.update(4, 5)
        self.assertEqual(rect.id, 4)
        self.assertEqual(rect.size, 5)
        self.assertEqual(rect.height, 5)
        rect.update(4, 5, 2)
        self.assertEqual(rect.size, 5)
        rect.update(4, 5, 2, 9)
        self.assertEqual(rect.x, 2)
        rect.update(4, 5, 2, 9)
        self.assertEqual(rect.y, 9)

    def test_update_method_with_kwargs(self):
        """
        test rectangle instance update method with args and kwargs.
        """

        rec = Square(2, 3)
        # only keywords arguments provided
        rec.update(id=10, size=1)
        self.assertEqual(rec.id, 10)
        self.assertEqual(rec.size, 1)

        # keyword arguments with positional arguments
        rec.update(2, 3, y=9, x=2)
        self.assertEqual(rec.x, 3)
        self.assertEqual(rec.y, 0)
        self.assertEqual(rec.id, 2)
        self.assertEqual(rec.size, 3)

        # keywords arguments all through
        rec.update(id=8, size=40, x=2, y=4)
        self.assertEqual(rec.x, 2)
        self.assertEqual(rec.y, 4)
        self.assertEqual(rec.id, 8)
        self.assertEqual(rec.width, 40)

    def test_update_to_raise_exceptions_t(self):
        """
        test update method to raise TypeError
        """

        rect = Square(1, 2, 3, 4)

        # tests with strings
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            rect.update(id=2, width="2", x=5)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            rect.update(2, -9)
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            rect.update(2, 3, 9, '9')
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            rect.update(2, 3, '9', 9)

        # tests with lists
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            rect.update(size=[2], x=2, id=[2], y=5)
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            rect.update(id=2, width=3, x=[4])
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            rect.update(x=2, width=3, height=9, y=[9, 3, 9])
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            rect.update(id=2, weight=3, y=9, height=9, x=[1, 4, 4.6])

        # tests with tuples
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            rect.update(2, (2, 4), 5)
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            rect.update(2, 3, (0, 2))
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            rect.update(2, 3, 3, (2, 8))

    def test_do_dictionary(self):
        """
        tests to_dictionary method.
        """

        r = Square(2, id=9)
        self.assertEqual(type(r.to_dictionary()), dict)
        self.assertEqual(r.to_dictionary(), {'id': 9, 'size': 2, 'x': 0,
                         'y': 0})
        r.update(x=1, y=2)
        self.assertEqual(type(r.to_dictionary()), dict)
        self.assertEqual(r.to_dictionary(), {'id': 9, 'size': 2, 'x': 1,
                         'y': 2})

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_to_json_string_output(self, mock_stdout):
        """
        test json string representation printed to stdout
        """

        r = Square(2, id=900)

        print(r.to_json_string([r.to_dictionary()]))

        captured = mock_stdout.getvalue()
        self.assertEqual(captured,
                         '[{"id": 900, "size": 2, "x": 0, "y": 0}]\n')

    def test_to_json_string_(self):
        """
        test json string representation.
        """

        r = Square(2, 4, id=900)

        self.assertEqual(r.to_json_string([r.to_dictionary()]),
                         '[{"id": 900, "size": 2, "x": 4, "y": 0}]')

        r.update(5, 8, 6, 4)
        self.assertEqual(r.to_json_string([r.to_dictionary()]),
                         '[{"id": 5, "size": 8, "x": 6, "y": 4}]')

    def test_to_json_string_multiple(self):
        """
        test json string representation for more than one instance.
        """

        r = Square(2, id=900)
        r2 = Square(2, 6, 9, 10)

        self.assertEqual(r.to_json_string([r.to_dictionary(),
                         r2.to_dictionary()]),
                         '[{"id": 900, "size": 2, "x": 0, "y": 0}, ' +
                         '{"id": 10, "size": 2, "x": 6, "y": 9}]')

        r.update(5, 8, 6, 4)
        self.assertEqual(r.to_json_string([r.to_dictionary()]),
                         '[{"id": 5, "size": 8, "x": 6, "y": 4}]')

    def test_create(self):
        """
        tests class method create
        """

        s = self.s1.create(**{'id': 90, 'x': 2, 'y': 10, 'size': 10})

        self.assertEqual(str(s), '[Square] (90) 2/10 - 10')

    def test_save_to_file(self):
        """
        tests save to file method.
        """

        r1 = Square(2, 6, 7, 98)

        r2 = r1.create(**r1.to_dictionary())

        r1.save_to_file([r1, r2])

        with open("Square.json", 'r', encoding='utf-8') as f:
            string = f.read()
        self.assertEqual(string, '[{"id": 98, "size": 2,' +
                         ' "x": 6, "y": 7}, ' +
                         '{"id": 98, "size": 2, "x": 6, "y": ' +
                         '7}]')

        Square.save_to_file([])
        with open("Square.json", 'r', encoding='utf-8') as f:
            string = f.read()
        self.assertEqual(string, '[]')
        Square.save_to_file(None)

        with open("Square.json", 'r', encoding='utf-8') as f:
            string = f.read()
        self.assertEqual(string, '[]')

        r = Square(1)
        Square.save_to_file([r1])
        with open("Square.json", 'r', encoding='utf-8') as f:
            string = f.read()
        self.assertEqual(string, Square.to_json_string([r1.to_dictionary()]
                                                       ))

    def test_from_json_string(self):
        """
        tests from json string method.
        """

        squares = [self.s1.to_dictionary(), self.s3.to_dictionary()]
        json_obj = self.s1.to_json_string(squares)
        py_obj = self.s1.from_json_string(json_obj)

        self.assertEqual(squares, py_obj)

    def test_to_json_empty_None(self):
        """
        test to json method with None or empty list as argument.
        """

        s = Square.to_json_string([])
        self.assertEqual(s, '[]')

        s = Square.to_json_string(None)
        self.assertEqual(s, '[]')

    def test_load_from_file(self):
        """
        tests load from file method
        """

        r1 = Square(2, 3, id=90)
        Square.save_to_file([r1])

        obj = Square.load_from_file()

        self.assertEqual(str(r1), str(obj[0]))

    def from_load_from_non_existing_file(self):
        """
        tests loading from non exisiting file"""

        if os.path("Square.json"):
            os.remove("Square.json")
        data = Square.load_from_file()

        self.assertEqual(data, [])
