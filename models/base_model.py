#!/usr/bin/python3

"""
BaseModel Module
"""

from datetime import datetime
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

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Returns informal string representation of an instance
        """
        return f"[{self.__class__.__name__} ({self.id}) {self.__dict__}]"

    def save(self):
        """
        Updates the public instance (updated_at) with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all key/value pairs of __dict__ of an instance
        """
        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        return self.__dict__
