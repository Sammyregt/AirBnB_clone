#!/usr/bin/python3
"""
    Defines place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
        Defines Place class
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_bathrooms = 0
    number_rooms = 0
    max_guest = 0
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenity_ids = []
