#!/usr/bin/python3
"""
A class MyList that inherits from list
"""


class MyList(list):
    """ class body """

    def __init__(self, initial_list):
        """ init body """
        for element in initial_list:
            if not isinstance(element, int):
                raise TypeError("elements must be an integer")
        return super().__init__(initial_list)

    def print_sorted(self):
        """ method body """
        sorted_list = sorted(self)
        print(sorted_list)
