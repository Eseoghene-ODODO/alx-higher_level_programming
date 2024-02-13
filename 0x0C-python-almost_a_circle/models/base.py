#!/usr/bin/python3
"""
A base class
"""

import json
from os import path
import csv


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
        if list_dictionaries is None or len(list_dictionaries) == 0:
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
        if not json_string:
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

    @classmethod
    def load_from_file(cls):
        """returns a list of instances (convert json representations)"""
        file_load = "{}.json".format(cls.__name__)
        if not path.isfile(file_load):
            return []
        with open(file_load, "r", encoding="utf-8") as f:
            return [cls.create(**dic)
                    for dic in cls.from_json_string(f.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Converts 'list_objs' to csv format"""
        if not list_objs:
            list_objs = []
        with open("{}.csv".format(cls.__name__), 'w', encoding="utf-8") as fil:
            if cls.__name__ == "Rectangle":
                fields = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == "Square":
                fields = ['id', 'size', 'x', 'y']
            writer = csv.DictWriter(fil, fieldnames=fields)
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """method body"""
        list_objs = []
        with open("{}.csv".format(cls.__name__), 'r') as file_csv:
            if cls.__name__ == "Rectangle":
                fields = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == "Square":
                fields = ['id', 'size', 'x', 'y']
            reader = csv.DictReader(file_csv, fieldnames=fields)
            list_objs = []
            for row in reader:
                for key in row:
                    row[key] = int(row[key])
                list_objs.append(cls.create(**row))
        return list_objs
