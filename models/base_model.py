#!/usr/bin/python3

"""
BaseModel Module
"""

from datetime import datetime
import models
import uuid


class BaseModel:
    """
    Defines all common attributes/methods for other classes
    Attributes:
        Public instance:
            id (str): assigned with uuid when instance is created
            created_at (datetime): assigned with current datetime on instance creation
            updated_at (datetime): assigned with current datetime & updated when instance changes
    """

    def __init__(self, *args, **kwargs):
        if len(kwargs) > 0:
            kwargs.pop('__class__')
            for (k, v) in kwargs.items():
                if k in ["created_at", "updated_at"]:
                    self.__dict__[k] = datetime.fromisoformat(v)
                else:
                    self.__dict__[k] = v
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        Returns informal string representation of an instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}]"

    def save(self):
        """
        Updates the public instance (updated_at) with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all key/value pairs of __dict__ of an instance
        """
        a_dict = self.__dict__.copy()
        a_dict['__class__'] = self.__class__.__name__
        a_dict["created_at"] = self.created_at.isoformat()
        a_dict["updated_at"] = self.updated_at.isoformat()
        return (a_dict)
