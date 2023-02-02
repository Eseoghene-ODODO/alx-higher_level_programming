#!/usr/bin/python3
"""Module for LockedClass"""


class LockedClass:
    """A locked class that only lets the user create the instance
    attribute 'first_name'"""
    __slots__ = ['first_name']
