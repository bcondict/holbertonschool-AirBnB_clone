#!/usr/bin/python3
"""
    File Storage class.
"""


import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

Classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage():
    """
    FileStorage class attributes
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return the class attribute __object """
        return FileStorage.__objects

    def new(self, obj):
        """
            Creates a new class.id & value of an
            instance in __objects dictionary
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
            serializes __objects to the JSON file
        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="UTF-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """
            Deserializes the JSON file to __objetcs
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                file_obj = json.load(f).items
                for key in file_obj:
                    FileStorage.__objects[key] = Classes[file_obj[key]["__class__"]](**file_obj[key])
        except Exception:
            pass
