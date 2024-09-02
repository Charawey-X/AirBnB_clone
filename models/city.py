#!/usr/bin/python3

"""
City Module
"""

from datetime import datetime
import models
import uuid


class City(models.BaseModel):
    """
    Defines City model and inherits from Base
    Attributes:
        Public class attributes:
            name (str)
            state_id (str)
    """

    name = ""
    state_id = ""
