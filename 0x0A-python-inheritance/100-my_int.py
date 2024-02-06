#!/usr/bin/python3
"""
A class MyInt that inherits from int
"""


class MyInt(int):
    """ class body """

    def __eq__(self, other):
        """ method body """
        return super().__ne__(other)

    def __ne__(self, other):
        """ method body """
        return super().__eq__(other)
