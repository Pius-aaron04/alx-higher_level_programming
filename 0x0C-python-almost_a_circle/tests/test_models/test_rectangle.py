"""
contains test case for rectangle class
"""

import unittest
from unittest.mock import patch
import io
from models.rectangle import Rectangle
import os


class TestClassRectangle(unittest.TestCase):
    """
    tests the rectangle class.
    """

    def test_rectangle_inst_constr(self):
        """
        tests rectangle instance creation with invalid
        types
        """

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            rect = Rectangle("2", 5)
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            rect1 = Rectangle(3, "3")
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            rect = Rectangle([1, 3], (1, 2, 3))
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            rect = Rectangle(1, 4, "2")
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            rect = Rectangle(1, 2, 2, [5])
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            rect = Rectangle(-2, 5)

    def test_rectangle_inst_constr_val(self):
        """
        test Rectangle instances for value Errors.
        """

        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r = Rectangle(-2, 5)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r = Rectangle(0, 5)
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            r = Rectangle(2, -5)
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            r = Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            r = Rectangle(2, 5, -45)
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            r = Rectangle(2, 5, 4, -7)

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

        r1 = Rectangle(2, 5, 0, 0)
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

        self.assertEqual(rect1.id, rect1.id)
        self.assertEqual(rect2.id, rect1.id + 1)
        self.assertEqual(rect3.id, 5)
        self.assertEqual(rect4.id, rect2.id + 1)

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

    def test_rectangle_update_method(self):
        """
        tests the update method.
        """

        rect = Rectangle(2, 5, 7, 8, 89)
        rect.update(3)
        self.assertEqual(rect.id, 3)
        rect.update(4, 5)
        self.assertEqual(rect.id, 4)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 5)
        rect.update(4, 5, 2)
        self.assertEqual(rect.height, 2)
        rect.update(4, 5, 2, 9)
        self.assertEqual(rect.x, 9)
        rect.update(4, 5, 2, 9, 10)
        self.assertEqual(rect.y, 10)

    def test_update_method_with_kwargs(self):
        """
        test rectangle instance update method with args and kwargs.
        """

        rec = Rectangle(2, 3)
        # only keywords arguments provided
        rec.update(id=10, width=1, height=1)
        self.assertEqual(rec.id, 10)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 1)

        # keyword arguments with positional arguments
        rec.update(2, 3, 4, y=9, x=2)
        self.assertEqual(rec.x, 0)
        self.assertEqual(rec.y, 0)
        self.assertEqual(rec.id, 2)
        self.assertEqual(rec.width, 3)
        self.assertEqual(rec.height, 4)

        # keywords arguments all through
        rec.update(id=8, width=40, height=12, x=2, y=4)
        self.assertEqual(rec.x, 2)
        self.assertEqual(rec.y, 4)
        self.assertEqual(rec.id, 8)
        self.assertEqual(rec.width, 40)
        self.assertEqual(rec.height, 12)

    def test_update_to_raise_exceptions_t(self):
        """
        test update method to raise TypeError
        """

        rect = Rectangle(1, 2, 3, 4, 5)

        # tests with strings
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            rect.update(id=2, width="2", x=5)

        # tests with lists
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            rect.update(x=2, width=[2], y=5)
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            rect.update(id=2, width=3, height=[4])
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            rect.update(x=2, width=3, height=9, y=[9, 3, 9])
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            rect.update(id=2, weight=3, y=9, height=9, x=[1, 4, 4.6])

    def test_do_dictionary(self):
        """
        tests to_dictionary method.
        """

        r = Rectangle(2, 4, id=9)
        self.assertEqual(type(r.to_dictionary()), dict)
        self.assertEqual(r.to_dictionary(), {'id': 9, 'width': 2, 'height': 4,
                         'x': 0, 'y': 0})
        r.update(x=1, y=2)
        self.assertEqual(type(r.to_dictionary()), dict)
        self.assertEqual(r.to_dictionary(), {'id': 9, 'width': 2, 'height': 4,
                         'x': 1, 'y': 2})

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_to_json_string_output(self, mock_stdout):
        """
        test json string representation printed to stdout
        """

        r = Rectangle(2, 4, id=900)

        print(r.to_json_string([r.to_dictionary()]))

        captured = mock_stdout.getvalue()
        self.assertEqual(captured,
                         '[{"id": 900, "width": 2, "height": 4, "x": 0, '
                         '"y": 0}]' + '\n')

    def test_to_json_string_(self):
        """
        test json string representation.
        """

        r = Rectangle(2, 4, id=900)

        self.assertEqual(r.to_json_string([r.to_dictionary()]),
                         '[{"id": 900, "width": 2, "height": 4, "x": 0, ' +
                         '"y": 0}]')

        r.update(5, 8, 6, 4, 0)
        self.assertEqual(r.to_json_string([r.to_dictionary()]),
                         '[{"id": 5, "width": 8, "height": 6, "x": 4, ' +
                         '"y": 0}]')

    def test_to_json_string_multiple(self):
        """
        test json string representation for more than one instance.
        """

        r = Rectangle(2, 4, id=900)
        r2 = Rectangle(2, 3, 6, 9, 10)

        self.assertEqual(r.to_json_string([r.to_dictionary(),
                                           r2.to_dictionary()]),
                         '[{"id": 900, "width": 2, "height": 4, "x": 0,' +
                         ' "y": 0}, '
                         + '{"id": 10, "width": 2, "height": 3, "x": 6, ' +
                         '"y": 9}]')

        r.update(5, 8, 6, 4, 0)
        self.assertEqual(r.to_json_string([r.to_dictionary()]),
                         '[{"id": 5, "width": 8, "height": 6, "x": 4, "y":'
                         + ' 0}]')

    def test_create(self):
        """
        tests class method create
        """

        s1 = Rectangle(2, 5)
        s = s1.create(**{'id': 90, 'x': 2, 'y': 10, 'width': 10, 'height': 2})

        self.assertEqual(str(s), '[Rectangle] (90) 2/10 - 10/2')

    def test_save_to_file(self):
        """
        tests save to file method.
        """

        r1 = Rectangle(2, 5, 6, 7, 98)

        r2 = r1.create(**r1.to_dictionary())

        r1.save_to_file([r1, r2])

        with open("Rectangle.json", 'r', encoding='utf-8') as f:
            string = f.read()
        self.assertEqual(string, '[{"id": 98, "width": 2, "height": 5,' +
                         ' "x": 6, "y": 7}, ' +
                         '{"id": 98, "width": 2, "height": 5, "x": 6, "y": ' +
                         '7}]')
        r1.save_to_file([])

        with open("Rectangle.json", 'r', encoding='utf-8') as f:
            string = f.read()
        self.assertEqual(string, '[]')
        Rectangle.save_to_file(None)

        with open("Rectangle.json", 'r', encoding='utf-8') as f:
            string = f.read()
        self.assertEqual(string, '[]')

        r = Rectangle(1, 2)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", 'r', encoding='utf-8') as f:
            string = f.read()
        self.assertEqual(string, Rectangle.to_json_string([r1.to_dictionary()]
                                                          ))

    def test_from_json_string(self):
        """
        tests from json string method.
        """

        r1 = Rectangle(2, 4, id=900)
        r3 = Rectangle(2, 3, 6, 9, 10)

        recs = [r1.to_dictionary(), r3.to_dictionary()]
        json_obj = Rectangle.to_json_string(recs)
        py_obj = r3.from_json_string(json_obj)

        self.assertEqual(recs, py_obj)

    def test_to_json_empty_None(self):
        """
        test to json method with None or empty list as argument.
        """

        s = Rectangle.to_json_string([])
        self.assertEqual(s, '[]')

        s = Rectangle.to_json_string(None)
        self.assertEqual(s, '[]')

    def test_load_from_file(self):
        """
        tests load from file method
        """

        r1 = Rectangle(2, 3, id=90)
        Rectangle.save_to_file([r1])

        obj = Rectangle.load_from_file()

        self.assertEqual(str(r1), str(obj[0]))

    def from_load_from_non_existing_file(self):
        """
        tests loading from non exisiting file"""

        if os.path("Rectangle.json"):
            os.remove("Rectangle.json")
        data = Rectangle.load_from_file()

        self.assertEqual(data, [])
