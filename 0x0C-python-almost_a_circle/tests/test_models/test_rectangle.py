#!/usr/bin/python3

"""Unittest for rectangle.py"""


import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class"""

    def test_init_with_id(self):
        """Test init with id"""
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 12)

    def test_init_without_id(self):
        """Test init without id"""
        Base._Base__nb_objects = 0
        r2 = Rectangle(10, 2)
        self.assertEqual(r2.id, 1)

    def test_init_with_more_args(self):
        """Test init with more args"""
        with self.assertRaises(TypeError):
            r3 = Rectangle(10, 2, 0, 0, 12, 13)

    def test_init_with_no_args(self):
        """Test init with no args"""
        with self.assertRaises(TypeError):
            r4 = Rectangle()

    def test_init_with_one_arg(self):
        """Test init with one arg"""
        with self.assertRaises(TypeError):
            r5 = Rectangle(1)

    def test_init_with_two_args(self):
        """Test init with two args"""
        r6 = Rectangle(1, 2)
        self.assertEqual(r6.width, 1)
        self.assertEqual(r6.height, 2)

    def test_width(self):
        """Test width"""
        r7 = Rectangle(10, 2)
        self.assertEqual(r7.width, 10)

    def test_width_setter(self):
        """Test width setter"""
        r8 = Rectangle(10, 2)
        r8.width = 20
        self.assertEqual(r8.width, 20)

    def test_width_setter_with_string(self):
        """Test width setter with string"""
        with self.assertRaises(TypeError):
            r9 = Rectangle(10, 2)
            r9.width = "hello"

    def test_width_setter_with_zero(self):
        """Test width setter with zero"""
        with self.assertRaises(ValueError):
            r10 = Rectangle(10, 2)
            r10.width = 0

    def test_width_setter_with_negative(self):
        """Test width setter with negative"""
        with self.assertRaises(ValueError):
            r11 = Rectangle(10, 2)
            r11.width = -10

    def test_height(self):
        """Test height"""
        r12 = Rectangle(10, 2)
        self.assertEqual(r12.height, 2)

    def test_height_setter(self):
        """Test height setter"""
        r13 = Rectangle(10, 2)
        r13.height = 20
        self.assertEqual(r13.height, 20)

    def test_height_setter_with_string(self):
        """Test height setter with string"""
        with self.assertRaises(TypeError):
            r14 = Rectangle(10, 2)
            r14.height = "hello"

    def test_height_setter_with_zero(self):
        """Test height setter with zero"""
        with self.assertRaises(ValueError):
            r15 = Rectangle(10, 2)
            r15.height = 0

    def test_height_setter_with_negative(self):
        """Test height setter with negative"""
        with self.assertRaises(ValueError):
            r16 = Rectangle(10, 2)
            r16.height = -10

    def test_error_messages(self):
        """Test error messages"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r17 = Rectangle("hello", 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r18 = Rectangle(10, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r19 = Rectangle(10, 2, "hello", 0)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r20 = Rectangle(10, 2, 0, "hello")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r21 = Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r22 = Rectangle(10, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r23 = Rectangle(10, 2, -1, 0)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r24 = Rectangle(10, 2, 0, -1)

    def test_area(self):
        """Test area"""
        r25 = Rectangle(3, 2)
        self.assertEqual(r25.area(), 6)

    def test_area_with_args(self):
        """Test area with args"""
        with self.assertRaises(TypeError):
            r26 = Rectangle(3, 2)
            r26.area(1)

    def test_display(self):
        """Test display"""
        r27 = Rectangle(2, 2)
        previous_stdout = sys.stdout
        result = io.StringIO()
        sys.stdout = result
        r27.display()
        sys.stdout = previous_stdout
        self.assertEqual(result.getvalue(), "##\n##\n")

    def test_display_with_args(self):
        """Test display with args"""
        with self.assertRaises(TypeError):
            r28 = Rectangle(2, 2)
            r28.display(1)

    def test_str(self):
        """Test str"""
        r29 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r29), "[Rectangle] (12) 2/1 - 4/6")

    def test_update(self):
        """Test update"""
        r30 = Rectangle(10, 10, 10, 10)
        r30.update(89)
        self.assertEqual(str(r30), "[Rectangle] (89) 10/10 - 10/10")
        r30.update(89, 2)
        self.assertEqual(str(r30), "[Rectangle] (89) 10/10 - 2/10")
        r30.update(89, 2, 3)
        self.assertEqual(str(r30), "[Rectangle] (89) 10/10 - 2/3")
        r30.update(89, 2, 3, 4)
        self.assertEqual(str(r30), "[Rectangle] (89) 4/10 - 2/3")
        r30.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r30), "[Rectangle] (89) 4/5 - 2/3")

    def test_to_dictionary(self):
        """checks dictionary conversion"""
        Base._Base__nb_objects = 0
        r31 = Rectangle(10, 2, 1, 9)
        r31dict = r31.to_dictionary()
        comp_dict = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertTrue(r31dict == comp_dict)


if __name__ == "__main__":
    unittest.main()
