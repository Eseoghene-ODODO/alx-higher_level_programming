#!/usr/bin/python3
"""
A function that creates an Object fron a JSON file
"""

import json


def load_from_json_file(filename):
    """function body"""
    with open(filename) as f:
        return json.load(f)
