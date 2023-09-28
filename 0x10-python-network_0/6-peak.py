#!/usr/bin/python3

"""Find a peak in a list of unsorted integers."""

def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers."""
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
    return None
