#!/usr/bin/python3

"""
User Module
"""

from datetime import datetime
import models
import uuid


class User(models.BaseModel):
    """
    Defines User model and inherits from Base
    Attributes:
        Public class attributes:
            email (str)
            password (str)
            first_name (str)
            last_name (str)
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
