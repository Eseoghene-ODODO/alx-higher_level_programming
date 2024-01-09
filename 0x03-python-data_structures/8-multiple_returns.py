#!/usr/bin/python3
"""
A function that returns a tuple with length of a string and its
first character
"""


def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    return (len(sentence), sentence[0])
