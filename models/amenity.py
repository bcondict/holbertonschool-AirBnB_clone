#!/usr/bin/python3
""" amenity class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ class that inherit from BaseModel. """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Init method for amenity. """
        super().__init__(*args, **kwargs)
