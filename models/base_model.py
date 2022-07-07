#!/usr/bin/python3
"""
    base class that defines all common attributes.
"""


import uuid
from models import storage
from datetime import datetime


class BaseModel:
    """
        Class that defines Base model attributes and methods
    """
    def __init__(self, *args, **kwargs):
        """
            Create new instances according given arguments and store the info
        """
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
        """
            Modify the stdr output with a specific format
        """
        st = "[{:s}] ({:s}) {:s}"
        st = st.format(self.__class__.__name__, self.id, str(self.__dict__))
        return st

    def save(self):
        """
            Update the attribute updated_at with the current datetime
            and save changes in json file.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
            Return a Dictionary with specific attributes and format
        """
        my_dict = dict(self.__dict__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return my_dict
