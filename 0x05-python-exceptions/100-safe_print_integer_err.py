#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as err:
        from sys import stderr
        stderr.write("Exception: {}\n".format(err))
        return False
