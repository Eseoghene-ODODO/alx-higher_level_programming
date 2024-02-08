#!/usr/bin/python3
"""
A function that returns the dictionary decription with  simple data structure
for JSON serialization of an object
"""


def class_to_json(obj):
    """function body"""
    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()
    return {}
