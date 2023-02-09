#!/usr/bin/python3
"""Module for read_lines method"""


def read_lines(filename="", nb_lines=0):
    """
    Method that reads n lines of a text file (UTF8)
    and prints it to stdout
    """
    with open(filename, encoding="utf-8") as my_file_0:
        if nb_lines <= 0:
            print(my_file_0.read(), end="")
        else:
            for line in my_file_0:
                if nb_lines == 0:
                    break
                print(line, end="")
                nb_lines -= 1
