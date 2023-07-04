#!/usr/bin/python3

"""Defines a class TestMaxInteger for max_integer([...])"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test class that defines test cases for the max_integer function.
    """
    def test_positive_integers(self):
        """Test for positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)
        self.assertEqual(max_integer([1, 2, 4, 2, 3]), 4)

    def test_negative_integers(self):
        """Test for negative integers"""
        self.assertEqual(max_integer([-10, -20, -30, -40]), -10)
        self.assertEqual(max_integer([-2, -91, -31, -4]), -2)
        self.assertEqual(max_integer([0, -91, -31, -4]), 0)
        self.assertEqual(max_integer([-123, -91, -31, -4]), -4)

    def test_pos_neg_integers(self):
        """Test for positive and negative integers"""
        self.assertEqual(max_integer([-9, -14, 23, 98, -9, -100, -1, 0]), 98)

    def test_empty_list(self):
        """Test for an empty list"""
        self.assertIsNone(max_integer([]), None)

    def test_one_arg(self):
        """Test for passing one number to list"""
        self.assertEqual(max_integer([1]), 1)

    def test_none_argument(self):
        """Test for passing None"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_list_with_none(self):
        """Test for list with None as one of its elements"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, 4, None])

    def test_none_list(self):
        """Test for passing None as list"""
        self.assertIsNone(max_integer([None]), None)

    def test_integers_and_strings(self):
        """Test for passing a string in the list"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, 4, "2"])

    def test_string_numbers(self):
        """Test for passing a string of numbers in list"""
        self.assertEqual(max_integer(["1234"]), "1234")

    def test_same_integers(self):
        """Test for passing same integers in list"""
        self.assertEqual(max_integer([2, 2, 2, 2, 2]), 2)
        self.assertEqual(max_integer([-55, -55, -55, -55]), -55)

    def test_zero(self):
        """Test for passing a zero in the list"""
        self.assertEqual(max_integer([0]), 0)

    def test_dictionary(self):
        """Test for passing a dictionary as a list"""
        with self.assertRaises(TypeError):
            max_integer([{'key1': 1}, {'key2': 2}])

    def test_list_in_list(self):
        """Test for list within a list"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, 4, [1, 2, 3, 4]])

    def test_tuple_in_list(self):
        """Test for tuple within a list"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, 4, (1, 2, 3)])

    def test_set_in_list(self):
        """Test for set within a list"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, 4, {1, 2, 3}])

    def test_characters_list(self):
        """Test for list of characters"""
        self.assertEqual(max_integer(['a', 'c', 'd', 'v']), 'v')

    def test_numbers_character(self):
        """Test for a list of numbers and character/s"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, 's'])
        with self.assertRaises(TypeError):
            max_integer([-1, -2, -3, 's'])
        with self.assertRaises(TypeError):
            max_integer([1.1, 2.2, 3.3, 's'])
        with self.assertRaises(TypeError):
            max_integer([-1.1, 2.2, -3.3, 's'])

    def test_mixed_characters(self):
        """Test for a mixture of characters in list including +ve and -ve"""
        self.assertEqual(max_integer(['-a', '-d', '-k', '-w']), '-w')
        self.assertEqual(max_integer(['-a', '-d', 'k', '-w']), 'k')
        self.assertEqual(max_integer(['-a', 'z', 'k', '-w']), 'z')

    def test_mixed_list(self):
        """Test for a list containing various types"""
        with self.assertRaises(TypeError):
            max_integer([1, "87", 3, "hot", -3, [78], {87}, '-z', 'a'])

    def test_float_numbers(self):
        """Test for float numbers in a list including +ve and -ve"""
        self.assertEqual(max_integer([9.1, 2.3, 6.8, 0.1]), 9.1)
        self.assertEqual(max_integer([9, 2, 6.8, 0.1]), 9)
        self.assertEqual(max_integer([-9.1, -2.3, 6.8, 0.1]), 6.8)
        self.assertEqual(max_integer([-9, -2, -6.8, -0.1]), -0.1)
        self.assertEqual(max_integer([-9, -2, -6.8, 0.1]), 0.1)


if __name__ == '__main__':
    unittest.main()
