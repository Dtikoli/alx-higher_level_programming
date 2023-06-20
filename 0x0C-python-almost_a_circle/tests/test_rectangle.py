#!/usr/bin/python3
"""A unittests module for models/rectangle.py class.
Unittest classes:
    line 25 - TestRectangle_instantiation
    line 114 - TestRectangle_width
    line 190 - TestRectangle_height
    line 266 - TestRectangle_x
    line 338 - TestRectangle_y
    line 406 - TestRectangle_orderof_initialization
    line 457 - TestRectangle_area
    line 541 - TestRectangle_update_args
    line 679 - TestRectangle_update_kwargs
    line 791 - TestRectangle_others
"""
import io
import sys
import unittest
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_insantiation(unittest.TestCase):
    """Unittests for testing the Rectangle class instantiation."""

    def test_isbase_subclass(self):
        self.assertIsInstance(Rectangle(3, 4), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        rec1 = Rectangle(3, 4)
        rec2 = Rectangle(4, 3)
        self.assertEqual(rec1.id + 1, rec2.id)

    def test_three_args(self):
        rec1 = Rectangle(3, 4, 6)
        rec2 = Rectangle(4, 3, 2)
        self.assertEqual(rec1.id + 1, rec2.id)

    def test_four_args(self):
        rec1 = Rectangle(3, 4, 6, 8)
        rec2 = Rectangle(4, 3, 3, 5)
        self.assertEqual(rec1.id + 1, rec2.id)

    def test_five_args(self):
        self.assertEqual(Rectangle(10, 2, 0, 0, 4).id, 4)

    def test_over_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(8, 6, 3, 4, 5, 2)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 3).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 3).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 3).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 3, 0, 0, 1).__y)

    def test_width_getter(self):
        rec = Rectangle(4, 3, 2, 6, 1)
        self.assertEqual(rec.width, 4)

    def test_width_setter(self):
        rec = Rectangle(4, 3, 2, 6, 1)
        rec.width = 8
        self.assertEqual(rec.width, 8)

    def test_height_getter(self):
        rec = Rectangle(4, 3, 2, 6, 1)
        self.assertEqual(rec.height, 3)

    def test_height_setter(self):
        rec = Rectangle(4, 3, 2, 6, 1)
        rec.height = 6
        self.assertEqual(rec.height, 6)

    def test_x_getter(self):
        rec = Rectangle(4, 3, 2, 6, 1)
        self.assertEqual(rec.x, 2)

    def test_x_setter(self):
        rec = Rectangle(4, 3, 2, 6, 1)
        rec.x = 4
        self.assertEqual(rec.x, 4)

    def test_y_getter(self):
        rec = Rectangle(4, 3, 2, 6, 1)
        self.assertEqual(rec.y, 6)

    def test_y_setter(self):
        rec = Rectangle(4, 3, 2, 6, 1)
        rec.y = 12
        self.assertEqual(rec.y, 12)


class TestRectangle_width(unittest.TestCase):
    """Unittests for testing the Rectangle width attribute."""

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 3)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("string", 3)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(4.0, 3)

    def test_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(4), 3)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"kofi": 4, "Ama": 6}, 3)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 3)

    def test_bool_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 3)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([4, 6, 8], 3)

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((4, 6, 8), 3)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({4, 6, 8}, 3)

    def test_frozenset_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({2, 4, 6, 1}), 2)

    def test_range_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(4), 3)

    def test_bytes_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Python', 3)

    def test_bytearray_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'abcdefg'), 3)

    def test_memoryview_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'abcedfg'), 3)

    def test_inf_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 3)

    def test_nan_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 3)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-4, 3)


class TestRectangle_height(unittest.TestCase):
    """Unittests for testing the Rectangle height attribute."""

    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "str")

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(4, 0)

    def test_bool_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, True)

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, 3.0)

    def test_complex_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, complex(3))

    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, {"Kofi": 4, "Ama": 1})

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, [3, 6, 9])

    def test_set_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, {3, 6, 9})

    def test_tuple_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, (3, 6, 9))

    def test_frozenset_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, frozenset({3, 6, 9, 1}))

    def test_range_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, range(3))

    def test_bytes_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, b'Python')

    def test_bytearray_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, bytearray(b'abcdefg'))

    def test_memoryview_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, memoryview(b'abcedfg'))

    def test_inf_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, float('inf'))

    def test_nan_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, float('nan'))

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(4, -3)


class TestRectangle_x(unittest.TestCase):
    """Unittests for testing the Rectangle x attribute."""

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid", 2)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 5.5, 9)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, complex(5))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"a": 1, "b": 2}, 2)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, True, 2)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3], 2)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {1, 2, 3}, 2)

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (1, 2, 3), 2)

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, frozenset({1, 2, 3, 1}))

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, range(5))

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, b'Python')

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, bytearray(b'abcdefg'))

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, memoryview(b'abcedfg'))

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('inf'), 2)

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('nan'), 2)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 3, -1, 0)


class TestRectangle_y(unittest.TestCase):
    """Unittests for testing the Rectangle y attribute."""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, "invalid")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 5.5)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, complex(5))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {"a": 1, "b": 2})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, [1, 2, 3])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {1, 2, 3})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, (1, 2, 3))

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, frozenset({1, 2, 3, 1}))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, range(5))

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, b'Python')

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, bytearray(b'abcdefg'))

    def test_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, memoryview(b'abcedfg'))

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float('inf'))

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float('nan'))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 0, -1)


class TestRectangle_orderof_initialization(unittest.TestCase):
    """Unittests for testing the order of attributes for initialization"""

    def test_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", "invalid height")

    def test_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 3, "invalid x")

    def test_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid width", 2, 3, "invalid y")

    def test_height_before_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, "invalid height", "invalid x")

    def test_height_before_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid height", 2, "invalid y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid x", "invalid y")


class TestRectangle_area(unittest.TestCase):
    """Unittests for testing the area method of the Rectangle class."""

    def test_area_small(self):
        rec = Rectangle(4, 3, 0, 0, 0)
        self.assertEqual(rec.area(), 12)

    def test_area_large(self):
        rec = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(rec.area(), 999999999999998999000000000000001)

    def test_area_changed_attributes(self):
        rec = Rectangle(4, 3, 1, 1, 1)
        rec.width = 5
        rec.height = 4
        self.assertEqual(rec.area(), 20)

    def test_area_one_arg(self):
        rec = Rectangle(4, 3, 1, 1, 1)
        with self.assertRaises(TypeError):
            rec.area(1)


class TestRectangle_stdout(unittest.TestCase):
    """Unittests for testing __str__ and display methods of Rectangle class."""

    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns texts printed to stdout.
        Args:
            rect (Rectangle): The Rectangle to print to stdout.
            method (str): The method to run on rect.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    # Test __str__ method
    def test_str_method_print_width_height(self):
        rec = Rectangle(4, 3)
        capture = TestRectangle_stdout.capture_stdout(rec, "print")
        correct = f"[Rectangle] ({rec.id}) 0/0 - 4/3\n"
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_width_height_x(self):
        rec = Rectangle(4, 3, 2)
        correct = f"[Rectangle] ({rec.id}) 2/0 - 4/3"
        self.assertEqual(correct, rec.__str__())

    def test_str_method_width_height_x_y(self):
        rec = Rectangle(4, 3, 2, 2)
        correct = f"[Rectangle] ({rec.id}) 2/2 - 4/3"
        self.assertEqual(correct, str(rec))

    def test_str_method_width_height_x_y_id(self):
        rec = Rectangle(12, 20, 2, 1, 6)
        self.assertEqual("[Rectangle] (6) 2/1 - 12/20", str(rec))

    def test_str_method_changed_attributes(self):
        rec = Rectangle(4, 3, 0, 0, [2])
        rec.width = 8
        rec.height = 6
        rec.x = 2
        rec.y = 2
        self.assertEqual("[Rectangle] ([2]) 2/2 - 8/6", str(rec))

    def test_str_method_one_arg(self):
        rec = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            rec.__str__(1)

    # Test display method
    def test_display_width_height(self):
        rec = Rectangle(2, 3, 0, 0, 0)
        capture = TestRectangle_stdout.capture_stdout(rec, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

    def test_display_width_height_x(self):
        rec = Rectangle(3, 2, 1, 0, 1)
        capture = TestRectangle_stdout.capture_stdout(rec, "display")
        self.assertEqual(" ###\n ###\n", capture.getvalue())

    def test_display_width_height_y(self):
        rec = Rectangle(4, 5, 0, 1, 0)
        capture = TestRectangle_stdout.capture_stdout(rec, "display")
        display = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_width_height_x_y(self):
        rec = Rectangle(2, 4, 3, 2, 0)
        capture = TestRectangle_stdout.capture_stdout(rec, "display")
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, capture.getvalue())

    def test_display_one_arg(self):
        rec = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            rec.display(1)


class TestRectangle_update_args(unittest.TestCase):
    """Unittests for testing the update args method of the Rectangle class."""

    # Test args
    def test_update_args_zero(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(rec))

    def test_update_args_one(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(40)
        self.assertEqual("[Rectangle] (40) 10/10 - 10/10", str(rec))

    def test_update_args_two(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(rec))

    def test_update_args_three(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(40, 2, 3)
        self.assertEqual("[Rectangle] (40) 10/10 - 2/3", str(rec))

    def test_update_args_four(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(40, 2, 3, 4)
        self.assertEqual("[Rectangle] (40) 4/10 - 2/3", str(rec))

    def test_update_args_five(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(40, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (40) 4/5 - 2/3", str(rec))

    def test_update_args_more_than_five(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(40, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (40) 4/5 - 2/3", str(rec))

    def test_update_args_None_id(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(None)
        correct = f"[Rectangle] ({rec.id}) 10/10 - 10/10"
        self.assertEqual(correct, str(rec))

    def test_update_args_None_id_and_more(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(None, 4, 5, 2)
        correct = f"[Rectangle] ({rec.id}) 2/10 - 4/5"
        self.assertEqual(correct, str(rec))

    def test_update_args_twice(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(60, 2, 3, 4, 5, 6)
        rec.update(40, 5, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (40) 3/2 - 5/4", str(rec))

    def test_update_args_invalid_width_type(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.update(40, "invalid")

    def test_update_args_width_zero(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rec.update(40, 0)

    def test_update_args_width_negative(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rec.update(40, -5)

    def test_update_args_invalid_height_type(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec.update(40, 2, "invalid")

    def test_update_args_height_zero(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rec.update(40, 1, 0)

    def test_update_args_height_negative(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rec.update(40, 1, -5)

    def test_update_args_invalid_x_type(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec.update(40, 2, 3, "invalid")

    def test_update_args_x_negative(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rec.update(40, 1, 2, -4)

    def test_update_args_invalid_y(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rec.update(40, 2, 3, 4, "invalid")

    def test_update_args_y_negative(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rec.update(40, 1, 2, 3, -1)

    def test_update_args_width_before_height(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.update(40, "invalid", "invalid")

    def test_update_args_width_before_x(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.update(40, "invalid", 1, "invalid")

    def test_update_args_width_before_y(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.update(40, "invalid", 1, 2, "invalid")

    def test_update_args_height_before_x(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec.update(40, 1, "invalid", "invalid")

    def test_update_args_height_before_y(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec.update(40, 1, "invalid", 1, "invalid")

    def test_update_args_x_before_y(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec.update(40, 1, 2, "invalid", "invalid")


class TestRectangle_update_kwargs(unittest.TestCase):
    """Unittests for testing the update kwargs method of Rectangle."""

    def test_update_kwargs_one(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(id=40)
        self.assertEqual("[Rectangle] (40) 10/10 - 10/10", str(rec))

    def test_update_kwargs_two(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(width=4, id=40)
        self.assertEqual("[Rectangle] (40) 10/10 - 4/10", str(rec))

    def test_update_kwargs_three(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(width=4, height=3, id=40)
        self.assertEqual("[Rectangle] (40) 10/10 - 4/3", str(rec))

    def test_update_kwargs_four(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(id=40, x=1, height=3, y=3, width=4)
        self.assertEqual("[Rectangle] (40) 1/3 - 4/3", str(rec))

    def test_update_kwargs_five(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(y=5, x=8, id=40, width=4, height=3)
        self.assertEqual("[Rectangle] (40) 8/5 - 4/3", str(rec))

    def test_update_kwargs_None_id(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(id=None)
        correct = f"[Rectangle] ({rec.id}) 10/10 - 10/10"
        self.assertEqual(correct, str(rec))

    def test_update_kwargs_None_id_and_more(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(id=None, height=3, y=9)
        correct = f"[Rectangle] ({rec.id}) 10/9 - 10/3"
        self.assertEqual(correct, str(rec))

    def test_update_kwargs_twice(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(id=40, x=1, height=5)
        rec.update(y=3, height=3, width=4)
        self.assertEqual("[Rectangle] (40) 1/3 - 4/3", str(rec))

    def test_update_kwargs_invalid_width_type(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rec.update(width="invalid")

    def test_update_kwargs_width_zero(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rec.update(width=0)

    def test_update_kwargs_width_negative(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rec.update(width=-5)

    def test_update_kwargs_invalid_height_type(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rec.update(height="invalid")

    def test_update_kwargs_height_zero(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rec.update(height=0)

    def test_update_kwargs_height_negative(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rec.update(height=-5)

    def test_update_kwargs_inavlid_x_type(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rec.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rec.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rec.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rec.update(y=-5)

    def test_update_args_and_kwargs(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(40, 4, height=4, y=6)
        self.assertEqual("[Rectangle] (40) 10/10 - 4/10", str(rec))

    def test_update_kwargs_wrong_keys(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(a=5, b=10)
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(rec))

    def test_update_kwargs_some_wrong_keys(self):
        rec = Rectangle(10, 10, 10, 10, 10)
        rec.update(height=3, id=40, a=18, b=50, x=19, y=7)
        self.assertEqual("[Rectangle] (40) 19/7 - 10/3", str(rec))


class TestRectangle_others(unittest.TestCase):
    """Unittests for testing to_dictionary, create and load-from-file."""

    def setUp(self):
        """Method invoked for tests"""
        Base._Base__nb_objects = 0

    def test_to_dictionary_one(self):
        r1 = Rectangle(1, 2, 3, 4, 1)
        res = "[Rectangle] (1) 3/4 - 1/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 1)

        res = "<class 'dict'>\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(r1.to_dictionary()))
            self.assertEqual(str_out.getvalue(), res)

    def test_to_dictionary_two(self):
        r1 = Rectangle(2, 2, 2, 2)
        res = "[Rectangle] (1) 2/2 - 2/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r2 = Rectangle(5, 7)
        res = "[Rectangle] (2) 0/0 - 5/7\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r2)
            self.assertEqual(str_out.getvalue(), res)

        r1_dictionary = r1.to_dictionary()
        r2.update(**r1_dictionary)

        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.height, r2.height)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)
        self.assertEqual(r1.id, r2.id)

        res = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(r1_dictionary))
            self.assertEqual(str_out.getvalue(), res)

    def test_to_dictionary_output(self):
        rec = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, rec.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        rec1 = Rectangle(10, 2, 1, 9, 5)
        rec2 = Rectangle(5, 9, 1, 2, 10)
        rec2.update(**rec1.to_dictionary())
        self.assertNotEqual(rec1, rec2)

    def test_to_dictionary_arg(self):
        rec = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            rec.to_dictionary(1)

    def test_dict_to_json(self):
        r1 = Rectangle(2, 2)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        res = "[{}]\n".format(dictionary.__str__())

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dictionary)
            self.assertEqual(str_out.getvalue(), res.replace("'", "\""))

    def test_create_one(self):
        dictionary = {'id': 89}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)

    def test_create_two(self):
        dictionary = {'id': 89, 'width': 1}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)

    def test_create_three(self):
        dictionary = {'id': 89, 'width': 1, 'height': 2}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

    def test_create_four(self):
        dictionary = {'id': 89, 'width': 1, 'height': 2, 'x': 3}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)

    def test_create_five(self):
        dictionary = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_load_from_file_one(self):
        load_file = Rectangle.load_from_file()
        self.assertEqual(load_file, [])

    def test_load_from_file_two(self):
        r1 = Rectangle(5, 5)
        r2 = Rectangle(8, 2, 5, 5)

        linput = [r1, r2]
        Rectangle.save_to_file(linput)
        loutput = Rectangle.load_from_file()

        for i in range(len(linput)):
            self.assertEqual(linput[i].__str__(), loutput[i].__str__())

    def test_saving_to_file(self):
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        r1 = Rectangle(5, 10, 0, 0, 346)
        Rectangle.save_to_file([r1])

        with open("Rectangle.json", "r") as file:
            content = file.read()
        res = [{"x": 0, "y": 0, "id": 346, "height": 10, "width": 5}]
        self.assertEqual(res, json.loads(content))

    def test_saving_to_file_no_iter(self):
        r1 = Rectangle(5, 10)
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(r1)

    def test_saving_to_file_None(self):
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        r1 = Rectangle(5, 10, 0, 0, 346)
        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            content = file.read()

        self.assertEqual("[]", content)

    def test_saving_to_file_type(self):
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        r1 = Rectangle(5, 10, 0, 0, 346)
        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            content = file.read()

        self.assertEqual(str, type(content))
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass


if __name__ == "__main__":
    unittest.main()
