#!/usr/bin/python3
""" function that prints first and last name
    arg:
    first_name
    last_name
"""


def say_my_name(first_name, last_name=""):
    """condition to check the instance type
        arg type:
        string
        error type to raise TypeError"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is " + first_name + " " + last_name)
