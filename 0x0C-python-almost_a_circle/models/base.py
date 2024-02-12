#!/usr/bin/python3
"""
A base class
"""

import json


class Base:
    """class body"""
    __nb_objects = 0

    def __init__(self, id=None):
        """method body"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """method body"""
        if list_dictionaries == None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """method body"""
        if list_objs is None:
            list_objs = []
        with open(f"{cls.__name__}.json", "w", encoding='utf-8') as f:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """method body"""
        if json_string is None or json_string is []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """method body"""
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)
        else:
            return None
        dummy_instance.update(**dictionary)
        return dummy_instance
