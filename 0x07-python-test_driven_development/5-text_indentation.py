#!/usr/bin/python3
"""
A function that prints a text with 2 new lines \
after each of these characters: ., ? and :
"""


def  text_indentation(text):
    """ function body """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    chars = [".", "?", ":"]
    current_line = ""
    for characters in text:
        current_line += characters
        if characters in chars:
            print(current_line.strip())
            print()
            current_line = ""
    if current_line.strip():
        print(current_line.strip())
