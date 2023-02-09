#!/usr/bin/python3
"""Module for number_of_lines method"""


def number_of_lines(filename=""):
    """Method that returns the number of lines of a text file"""
    with open(filename, encoding="utf-8") as my_file_0:
        lineNum = 0
        while True:
            line = my_file_0.readline()
            if not line:
                break
            lineNum += 1
    return lineNum
