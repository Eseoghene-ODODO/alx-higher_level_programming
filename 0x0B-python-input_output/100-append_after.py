#!/usr/bin/python3
"""Module to append to a doc"""


def append_after(filename="", search_string="", new_string=""):
    """append function initialization"""

    text = ""
    with open(filename, "r+", encoding="utf-8") as file1:
        for line in file1:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as file2:
        file2.write(text)
