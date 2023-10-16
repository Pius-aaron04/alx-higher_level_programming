#!/usr/bin/python3
"""
contains definition for base class.
"""


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
        json_string = '['

        for dict_ in list_dictionaries:
            json_string += '{'
            # loops through each dict
            for key, value in dict_.items():
                if key != tuple(dict_.keys())[-1]:
                    json_string += '"{}": {}, '.format(key, value)
                else:
                    json_string += '"{}": {}'.format(key, value)
            if dict_ != list_dictionaries[-1]:
                json_string += '}, '
            else:
                json_string += '}'
        json_string += ']'
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

        print(objs)
        string = cls.to_json_string(objs)
        # opens a file with class name
        with open("{}.json".format(cls.__name__), 'w', encoding='utf-8') as f:
            f.write(string)

    @staticmethod
    def from_json_string(json_string):
        """
        extacts data from json string.
        """

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        creates a new instance with atrributes
        provided in the dictionary
        """

        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == 'Rectangle':
            new_instance = Rectangle(1, 1)
        elif cls.__name__ == 'Square':
            new_instance = Square(1)
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
        return json.loads(data)
