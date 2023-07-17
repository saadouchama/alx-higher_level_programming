#!/usr/bin/python3

"""
Module: `square`
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class: `Square`"""
    def __init__(self, size, x=0, y=0, id=None):
        """Init method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Str method"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update method"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """To dictionary method"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
