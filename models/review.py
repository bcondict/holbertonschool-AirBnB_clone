#!/usr/bin/python3
""" review class. """
from models.base_model import BaseModel


class Review(BaseModel):
    """ class that inherit from BaseModel. """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ Init method for review. """
        super().__init__(*args, **kwargs)
