#!/usr/bin/python3
"""
A function that reads a text file (UTF-8) and prints it to stdout
"""


def read_file(filename=""):
    """function body"""
    with open('my_file_0.txt', 'r', encoding='utf-8') as f:
        text_file = f.read()
        print(text_file)
