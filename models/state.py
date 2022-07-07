#!/usr/bin/python3
""" state class. """
from models.base_model import BaseModel


class State(BaseModel):
    """ class that inherit from BaseModel. """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Init method for state. """
        super().__init__(*args, **kwargs)
