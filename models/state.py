#!/usr/bin/python3

"""
State Module
"""

from datetime import datetime
import models
import uuid


class State(models.BaseModel):
    """
    Defines State model and inherits from Base
    Attributes:
        Public class attributes:
            name (str)
    """

    name = ""
