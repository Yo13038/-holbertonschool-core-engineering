#!/usr/bin/env python3
"""
module who print an integer follow by a new line
"""


def safe_print_integer(value):
    """
    function who handle exeption of a printed integer
    """

    try:
        print("{:d}".format(value))  # print asked format
        return True

    except (ValueError, TypeError):
        return False
