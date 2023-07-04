#!/usr/bin/python3

"""
This module contains a function that prints a text with 2 new lines after
"""


def text_indentation(text):
    """
    This function prints a text with 2 new lines after each occurrence
    of the characters: ., ? and :

    Args:
        text (str): The input text to be processed.

    Raises:
        TypeError: If the input text is not a string.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")
