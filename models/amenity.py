#!/usr/bin/python3

"""
Amenity Module
"""

from datetime import datetime
import models
import uuid


class Amenity(models.BaseModel):
    """
    Defines Amenity model and inherits from Base
    Attributes:
        Public class attributes:
            name (str)
    """

    name = ""
