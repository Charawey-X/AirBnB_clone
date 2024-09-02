#!/usr/bin/python3

"""
Review Module
"""

from datetime import datetime
import models
import uuid


class Review(models.BaseModel):
    """
    Defines Review model and inherits from Base
    Attributes:
        Public class attributes:
            place_id (str)
            user_id (str)
            text (str)
    """

    place_id = ""
    user_id = ""
    text = ""
