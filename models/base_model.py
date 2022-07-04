#!/usr/bin/python3
'''base class that defines all common attributes'''


import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """"""
    def __init__(self, *args, **kwargs):
        """ """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        my_format = "%Y-%m-%dT%H:%M:%S.%f"
        if bool(kwargs):
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, my_format)
                else:
                    self.__dict__[key] = value
        storage.new(self)

    def __str__(self):
        return("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        my_dict = self.__dict__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return my_dict
