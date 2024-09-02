#!/usr/bin/python3

"""
Place Module
"""

from datetime import datetime
import models
import uuid


class Place(models.BaseModel):
    """
    Defines Place model and inherits from Base
    Attributes:
        Public class attributes:
            city_id (str)
            user_id (str)
            name (str)
            description (str)
            number_rooms (int)
            number_bathrooms (int)
            max_guest (int)
            price_by_night (int)
            latitude (float)
            longitude (float)
            amenity_ids (list)
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
