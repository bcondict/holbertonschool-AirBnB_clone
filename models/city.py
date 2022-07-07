#!/usr/bin/python3
""" city class """
from models.base_model import BaseModel


class City(BaseModel):
    """ class that inherit from BaseModel. """
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """ Init method for city. """
        super().__init__(*args, **kwargs)
