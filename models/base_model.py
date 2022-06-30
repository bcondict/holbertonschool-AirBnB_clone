#!/usr/bin/python3
'''base class that defines all common attributes'''


import uuid
from datetime import datetime


class BaseModel:
    """"""
    def __init__(self, *args, **kwargs):
        """ """
        self.id = str(uuid.uuid4())

        self.created_at = str(datetime.now().isoformat())
        self.updated_at = str(datetime.now().isoformat())

    def __str__(self):
        return("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        my_dict = self.__dict__
        my_dict["__class__"] = self.__class__.__name__
        return my_dict
