#!/usr/bin/python3

"""
File Storage Module
"""

import json


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    Attributes:
        Private class:
            __file_path (str): path to the JSON file
            __objects (dict): stores all objects by <class name>.id
    """
    __file_path = ""
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj.__dict__

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        with open(self.__file_path, mode='w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects only if the JSON file (__file_path) exists
        If the file doesn’t exist, no exception should be raised
        """
        try:
            with open(self.__file_path, mode='r') as f:
                self.__objects = json.load(f)
        except:
            pass
