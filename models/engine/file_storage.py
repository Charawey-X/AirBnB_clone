#!/usr/bin/python3

"""
File Storage Module
"""

import models
import json


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    Attributes:
        Private class:
            __file_path (str): path to the JSON file
            __objects (dict): stores all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        if obj is not None:
            FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        """
        objects = {}
        for k, v in FileStorage.__objects.items():
            objects[k] = v.to_dict()
        with open(FileStorage.__file_path, mode='w') as f:
            json.dump(objects, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects only if the JSON file (__file_path) exists
        If the file doesn’t exist, no exception should be raised
        """
        try:
            with open(FileStorage.__file_path, mode='r') as f:
                for (k, v) in json.load(f).items():
                    cls = models.classes[v["__class__"]]
                    self.new(cls(**v))
        except FileNotFoundError:
            pass
