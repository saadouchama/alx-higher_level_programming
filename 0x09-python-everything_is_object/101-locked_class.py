#!/usr/bin/python3

"""Module for LockedClass."""


class LockedClass:
    """
    Prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name.

    Attributes:
        first_name (str): first name of something.
    """

    # The __slots__ attribute restricts the instance attributes
    # to only those listed. In this case, it allows only 'first_name'
    # to be set as an instance attribute.
    __slots__ = ["first_name"]

    def __init__(self, first_name=""):
        """Initializes the instance.

        Args:
            first_name (str): The value for the 'first_name'
                attribute (default: "").
        """
        self.first_name = first_name
