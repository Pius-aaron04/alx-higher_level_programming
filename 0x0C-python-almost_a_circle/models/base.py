#!/usr/bin/python3
"""
contains definition for base class.
"""

import csv
import json


class Base:
    """
    Base class for this project.
    """

    # private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializes instance attributes.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def validate_value(self, name, value):
        """
        validates value.
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if name in ('width', 'height') and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        converts dictionaries to json string
        """

        if list_dictionaries is None:
            return '[]'
        json_string = json.dumps(list_dictionaries)

        return json_string

    @classmethod
    def save_to_file(cls, list_objs):
        """
        saves json string representation of list_objs to a file.
        """

        objs = []
        if list_objs is None:
            list_objs = []
        for obj in list_objs:
            objs.append(obj.to_dictionary())

        string = cls.to_json_string(objs)
        # opens a file with class name
        with open("{}.json".format(cls.__name__), 'w', encoding='utf-8') as f:
            f.write(string)

    @staticmethod
    def from_json_string(json_string):
        """
        extacts data from json string.
        """

        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        creates a new instance with atrributes
        provided in the dictionary
        """

        from models.rectangle import Rectangle
        from models.square import Square

        new_instance = cls(1, 2)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """
        loads json object from file
        """

        try:
            with open("{}.json".format(cls.__name__, 'r',
                      encoding='utf-8')) as f:
                data = f.read()
        except FileNotFoundError:
            return []
        data = cls.from_json_string(data)
        instances = []
        for dict_ in data:
            instances.append(cls.create(**dict_))
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Saves objs to a csv file
        """

        with open("{}.csv".format(cls.__name__), 'w', encoding='utf-8') as f:
            csv_write = csv.writer(f)
            for obj_ in list_objs:
                csv_write.writerow(list(obj_.to_dictionary().values()))

    @classmethod
    def load_from_file_csv(cls):
        """
        loads attribute info from csv file
        """

        from models.rectangle import Rectangle
        from models.square import Square
        try:
            with open("{}.csv".format(cls.__name__), 'r',
                      encoding='utf-8') as f:
                reader = csv.reader(f)
                objs = []
                for row in reader:
                    instance = cls(1, 2)
                    attributes = [int(s) for s in row]
                    instance.update(*attributes)
                    objs.append(instance)
        except FileNotFoundError:
            return []

        return objs
