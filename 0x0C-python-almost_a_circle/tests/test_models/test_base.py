#!/usr/bin/python3

"""Unittest for base.py"""

import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def test_init_with_id(self):
        """Test __init__ with id"""
        Base._Base__nb_objects = 0
        b1 = Base(id=12)
        self.assertEqual(b1.id, 12)

    def test_init_without_id(self):
        """Test __init__ without id"""
        Base._Base__nb_objects = 0
        b2 = Base()
        self.assertEqual(b2.id, 1)

    def test_init_with_string(self):
        """Test __init__ with string"""
        Base._Base__nb_objects = 0
        b3 = Base("hello")
        self.assertEqual(b3.id, "hello")

    def test_init_with_float(self):
        """Test __init__ with float"""
        b4 = Base(3.14)
        self.assertEqual(b4.id, 3.14)

    def test_to_json_string_with_none(self):
        """Test to_json_string with None"""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_with_empty_list(self):
        """Test to_json_string with empty list"""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_with_one_dictionary(self):
        """Test to_json_string with one dictionary"""
        self.assertEqual(Base.to_json_string([{"id": 12}]), '[{"id": 12}]')

    def test_to_json_string_with_two_dictionaries(self):
        """Test to_json_string with two dictionaries"""
        self.assertEqual(Base.to_json_string([{"id": 12}, {"id": 13}]),
                         '[{"id": 12}, {"id": 13}]')

    def test_to_json_string_with_more_args(self):
        """Test to_json_string with more args"""
        with self.assertRaises(TypeError):
            Base.to_json_string([{"id": 12}, {"id": 13}], 1)

    def test_to_json_string_with_no_args(self):
        """Test to_json_string with no args"""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_save_to_file_with_none(self):
        """Test save_to_file with None"""
        Base.save_to_file(None)
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_with_empty_list(self):
        """Test save_to_file with empty list"""
        Base.save_to_file([])
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_with_one_dictionary(self):
        """Test save_to_file with one dictionary"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        a_dict = [r1.to_dictionary()]
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as file:
            list_dict = json.loads(file.read())
        self.assertTrue(a_dict == list_dict)

    def test_save_to_file_with_two_dictionaries(self):
        """Test save_to_file with two dictionaries"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        a_dict = [r1.to_dictionary(), r2.to_dictionary()]
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            list_dict = json.loads(file.read())
        self.assertTrue(a_dict == list_dict)

    def test_save_to_file_with_more_args(self):
        """Test save_to_file with more args"""
        with self.assertRaises(TypeError):
            Base.save_to_file([{"id": 12}, {"id": 13}], 1)

    def test_save_to_file_with_no_args(self):
        """Test save_to_file with no args"""
        with self.assertRaises(TypeError):
            Base.save_to_file()

    def test_from_json_string_with_none(self):
        """Test from_json_string with None"""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_with_empty_string(self):
        """Test from_json_string with empty string"""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_with_one_dictionary(self):
        """Test from_json_string with one dictionary"""
        self.assertEqual(Base.from_json_string('[{"id": 12}]'), [{"id": 12}])

    def test_from_json_string_with_two_dictionaries(self):
        """Test from_json_string with two dictionaries"""
        self.assertEqual(Base.from_json_string('[{"id": 12}, {"id": 13}]'),
                         [{"id": 12}, {"id": 13}])

    def test_from_json_string_with_more_args(self):
        """Test from_json_string with more args"""
        with self.assertRaises(TypeError):
            Base.from_json_string([{"id": 12}, {"id": 13}], 1)

    def test_from_json_string_with_no_args(self):
        """Test from_json_string with no args"""
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_create_with_rectangle(self):
        """Test create with rectangle"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r1.__str__(), r2.__str__())
        self.assertFalse(r1 is r2)

    def test_create_with_square(self):
        """Test create with square"""
        r1 = Square(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertEqual(r1.__str__(), r2.__str__())
        self.assertFalse(r1 is r2)

    def test_load_from_file_with_rectangle(self):
        """Test load_from_file with rectangle"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertTrue([r1.__str__(), r2.__str__()] ==
                        [r.__str__() for r in list_rectangles_output])

    def test_load_from_file_with_square(self):
        """Test load_from_file with square"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertTrue([s1.__str__(), s2.__str__()] ==
                        [s.__str__() for s in list_squares_output])

    def test_load_from_file_with_more_args(self):
        """Test load_from_file with more args"""
        with self.assertRaises(TypeError):
            Base.load_from_file([{"id": 12}, {"id": 13}], 1)

    def test_load_from_file_with_no_args(self):
        """Test load_from_file with no args"""
        Base.load_from_file()
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_csv_with_none(self):
        """Test save_to_file_csv with None"""
        Base.save_to_file_csv(None)
        with open("Base.csv", "r") as f:
            self.assertEqual(f.read(), "\n")

    def test_save_to_file_csv_with_empty_list(self):
        """Test save_to_file_csv with empty list"""
        Base.save_to_file_csv([])
        with open("Base.csv", "r") as f:
            self.assertEqual(f.read(), "\n")

    def test_save_to_file_csv_with_more_args(self):
        """Test save_to_file_csv with more args"""
        with self.assertRaises(TypeError):
            Base.save_to_file_csv([{"id": 12}, {"id": 13}], 1)

    def test_save_to_file_csv_with_no_args(self):
        """Test save_to_file_csv with no args"""
        with self.assertRaises(TypeError):
            Base.save_to_file_csv()

    def test_load_from_file_csv_with_more_args(self):
        """Test load_from_file_csv with more args"""
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([{"id": 12}, {"id": 13}], 1)

    def test_load_from_file_csv_with_no_args(self):
        """Test load_from_file_csv with no args"""
        Base.load_from_file_csv()
        with open("Base.csv", "r") as file:
            self.assertEqual(file.read(), "\n")

    def test_save_to_file_csv_with_rectangle(self):
        """Test save_to_file_csv with rectangle"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertTrue([r1.__str__(), r2.__str__()] ==
                        [r.__str__() for r in list_rectangles_output])

    def test_save_to_file_csv_with_square(self):
        """Test save_to_file_csv with square"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file_csv(list_squares_input)
        list_squares_output = Square.load_from_file_csv()
        self.assertTrue([s1.__str__(), s2.__str__()] ==
                        [s.__str__() for s in list_squares_output])


if "__main__" == __name__:
    unittest.main()
