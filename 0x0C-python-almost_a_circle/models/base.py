#!/usr/bin/python3

"""
Base class for all other classes in this project
"""

import json
import csv


class Base:
    """
    Base class for all other classes in this project
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        convert list_dictionaries to JSON string

        Args:
            list_dictionaries (list): list of dictionaries
        Returns:
            JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        write JSON string representation of list_objs to a file
        args:
            list_objs (list): list of instances that inherit from Base
        """

        filename = cls.__name__ + ".json"

        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]

        json_string = cls.to_json_string(list_objs)
        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        return list of the JSON string representation json_string
        args:
            json_string (str): string representing a list of dictionaries
        returns:
            list of dictionaries
        """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        return an instance with all attributes already set
        args:
            dictionary (dict): dictionary of attributes to set
        returns:
            instance with all attributes set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        return a list of instances
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                list_dicts = cls.from_json_string(file.read())
            return [cls.create(**dictionary) for dictionary in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        write CSV string representation of list_objs to a file
        args:
            list_objs (list): list of instances that inherit from Base
        """

        filename = cls.__name__ + ".csv"

        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        else:
            list_objs = []

        with open(filename, "w") as file:
            if list_objs is not None:
                fieldnames = []
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """
        return a list of instances
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as file:
                list_dicts = csv.DictReader(file)
                list_dicts = [dict([key, int(value)]
                                   for key, value in dictionary.items())
                              for dictionary in list_dicts]
            return [cls.create(**dictionary) for dictionary in list_dicts]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        draw Rectangles and Squares using turtle
        """
        import turtle
        import random

        turtle.title("Rectangles and Squares")
        turtle.bgcolor("black")
        turtle.speed(0)
        turtle.hideturtle()

        colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        for rectangle in list_rectangles:
            turtle.color(random.choice(colors))
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.pendown()
            for i in range(2):
                turtle.forward(rectangle.width)
                turtle.left(90)
                turtle.forward(rectangle.height)
                turtle.left(90)

        for square in list_squares:
            turtle.color(random.choice(colors))
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for i in range(4):
                turtle.forward(square.size)
                turtle.left(90)

        turtle.exitonclick()
