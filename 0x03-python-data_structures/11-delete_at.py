#!/usr/bin/python3
"""
A function that deletes the item at a specific position in a list
"""


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = []
    for element in range(len(my_list)):
        if element == idx:
            continue
        new_list.append(my_list[element])
    return new_list
