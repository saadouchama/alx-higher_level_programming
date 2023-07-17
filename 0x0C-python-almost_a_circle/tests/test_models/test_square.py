#!/usr/bin/python3

"""
Unittest for square.py
"""

import unittest
import sys
import io
from models.base import Base
from models.square import Square


def capture_output(func):
    """Capture output"""
    previous_stdout = sys.stdout
    output = io.StringIO()
    sys.stdout = output
    func()
    sys.stdout = previous_stdout
    return output.getvalue()


class TestSquare(unittest.TestCase):
    """
    Test cases for Square class
    """

    def test_init_with_id(self):
        """Test init with id"""
        s1 = Square(10, 0, 0, 12)
        self.assertEqual(s1.id, 12)

    def test_init_without_id(self):
        """Test init without id"""
        Base._Base__nb_objects = 0
        s2 = Square(10, 2)
        self.assertEqual(s2.id, 1)

    def test_number_of_objects(self):
        """Test number of objects"""
        Base._Base__nb_objects = 0
        s3 = Square(10, 2)
        s4 = Square(10, 2)
        self.assertEqual(s4.id, 2)
        self.assertEqual(Base._Base__nb_objects, 2)

    def test_size(self):
        """Test size"""
        s5 = Square(10, 2)
        self.assertEqual(s5.size, 10)

    def test_size_setter(self):
        """Test size setter"""
        s6 = Square(10, 2)
        s6.size = 20
        self.assertEqual(s6.size, 20)

    def test_size_setter_with_string(self):
        """Test size setter with string"""
        with self.assertRaises(TypeError):
            s7 = Square("hello", 2)

    def test_size_setter_with_zero(self):
        """Test size setter with zero"""
        with self.assertRaises(ValueError):
            s8 = Square(0, 2)

    def test_size_setter_with_negative(self):
        """Test size setter with negative"""
        with self.assertRaises(ValueError):
            s9 = Square(-1, 2)

    def test_x(self):
        """Test x"""
        s10 = Square(10, 2)
        self.assertEqual(s10.x, 2)

    def test_x_setter(self):
        """Test x setter"""
        s11 = Square(10, 2)
        s11.x = 20
        self.assertEqual(s11.x, 20)

    def test_x_setter_with_string(self):
        """Test x setter with string"""
        with self.assertRaises(TypeError):
            s12 = Square(10, "hello")

    def test_x_setter_with_negative(self):
        """Test x setter with negative"""
        with self.assertRaises(ValueError):
            s13 = Square(10, -1)

    def test_y(self):
        """Test y"""
        s14 = Square(10, 2, 3)
        self.assertEqual(s14.y, 3)

    def test_y_setter(self):
        """Test y setter"""
        s15 = Square(10, 2, 3)
        s15.y = 30
        self.assertEqual(s15.y, 30)

    def test_y_setter_with_string(self):
        """Test y setter with string"""
        with self.assertRaises(TypeError):
            s16 = Square(10, 2, "hello")

    def test_y_setter_with_negative(self):
        """Test y setter with negative"""
        with self.assertRaises(ValueError):
            s17 = Square(10, 2, -1)

    def test_area(self):
        """Test area"""
        s18 = Square(10, 2)
        self.assertEqual(s18.area(), 100)

    def test_str(self):
        """Test str"""
        s21 = Square(10, 2, 3, 4)
        self.assertEqual(s21.__str__(), "[Square] (4) 2/3 - 10")

    def test_errors(self):
        """Test errors"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s22 = Square("hello", 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s23 = Square(0, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s24 = Square(10, "hello")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s25 = Square(10, -1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s26 = Square(10, 2, "hello")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s27 = Square(10, 2, -1)

    def test_display(self):
        """Check display"""
        Square._nb_instances = 0

        square1 = Square(5)
        output1 = capture_output(square1.display)
        self.assertEqual(output1, "#####\n#####\n#####\n#####\n#####\n")

        square2 = Square(2, 2)
        output2 = capture_output(square2.display)
        self.assertEqual(output2, "  ##\n  ##\n")

        square3 = Square(3, 1, 3)
        output3 = capture_output(square3.display)
        self.assertEqual(output3, "\n\n\n ###\n ###\n ###\n")

    def test_update(self):
        """Test update"""
        s28 = Square(10, 10, 10, 10)
        s28.update(89)
        self.assertEqual(s28.id, 89)
        s28.update(89, 2)
        self.assertEqual(s28.size, 2)
        s28.update(89, 2, 3)
        self.assertEqual(s28.x, 3)
        s28.update(89, 2, 3, 4)
        self.assertEqual(s28.y, 4)

    def test_update_args(self):
        """Test update with *args"""
        s29 = Square(10, 10, 10, 10)
        s29.update(89, 2, 3, 4)
        self.assertEqual(s29.id, 89)
        self.assertEqual(s29.size, 2)
        self.assertEqual(s29.x, 3)
        self.assertEqual(s29.y, 4)

    def test_update_kwargs(self):
        """Test update with **kwargs"""
        s30 = Square(10, 10, 10, 10)
        s30.update(size=1)
        self.assertEqual(s30.size, 1)
        s30.update(size=1, x=2)
        self.assertEqual(s30.size, 1)
        self.assertEqual(s30.x, 2)
        s30.update(y=1, size=2, x=3, id=89)
        self.assertEqual(s30.id, 89)
        self.assertEqual(s30.size, 2)
        self.assertEqual(s30.x, 3)
        self.assertEqual(s30.y, 1)

    def test_update_errors(self):
        """Test update errors"""
        s31 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s31.update(89, "hello")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s31.update(89, 0)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s31.update(89, 10, "hello")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s31.update(89, 10, -1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s31.update(89, 10, 10, "hello")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s31.update(89, 10, 10, -1)

    def test_to_dictionary(self):
        """Test to_dictionary"""
        s32 = Square(10, 2, 1, 1)
        a_dict = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        s32_dictionary = s32.to_dictionary()
        self.assertTrue(s32_dictionary == a_dict)


if __name__ == "__main__":
    unittest.main()
