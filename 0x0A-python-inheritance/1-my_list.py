#!/usr/bin/python3
"""
A class MyList that inherits from list
"""


class MyList(list):
    """ class body """

    def print_sorted(self):
        """ method body """
        sorted_list = sorted(self)
        print(sorted_list)
