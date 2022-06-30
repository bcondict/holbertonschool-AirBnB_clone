#!/usr/bin/python3
'''base class that defines all common attributes'''


import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        """ """
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.now())
        self.updated_at = str(datetime.now())

    
    def created_at_method(self):
        """
            assign with the  currente datetime when an instance is created
        """
        created_at = str(datetime.now())
        print(created_at.isoformat())

    def updated_at_method(self):
        """
            assign twith the current datetime when an instance is created
            and it will be updated every time you change your object
        """
        updated_at = str(datetime.now())
        print(updated_at.isoformat())
    

    def __str__(self):
        return("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        my_dict = self.__dict__
        return my_dict
