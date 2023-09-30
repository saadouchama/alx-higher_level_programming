#!/usr/bin/python3
""" Module that finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ Function that finds a peak in a list of unsorted integers """
    if not list_of_integers:
        return None

    def helper(start, end):
        if start == end:
            return list_of_integers[start]

        mid = (start + end) // 2
        if list_of_integers[mid] > list_of_integers[mid - 1] and list_of_integers[mid] > list_of_integers[mid + 1]:
            return list_of_integers[mid]
        elif list_of_integers[mid] < list_of_integers[mid - 1]:
            return helper(start, mid - 1)
        else:
            return helper(mid + 1, end)

    return helper(0, len(list_of_integers) - 1)
