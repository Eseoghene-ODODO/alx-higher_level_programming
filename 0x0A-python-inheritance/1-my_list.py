#!/usr/bin/python3
"""Module for class Mylist"""


class MyList(list):
    """"class Mylist that inherits from list"""

    def print_sorted(self):
        """method that prints sorted list"""

        print(sorted(self))
