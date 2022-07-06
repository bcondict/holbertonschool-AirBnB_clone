#!/usr/bin/python3
""""""


import json
# from models.base_model import BaseModel


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return the class attribute __object """
        return FileStorage.__objects

    def new(self, obj):
        key_name = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key_name] = obj.to_dict()
        # FileStorage.__objects["{}{}".
        #      format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict
        """

        with open(FileStorage.__file_path, mode="w", encoding="UTF-8") as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        my_file = FileStorage.__file_path
        try:
            with open(my_file, mode="r", encoding="utf-8") as f:
                FileStorage.__objects = json.load(f)

        except Exception:
            pass
        # FileStorage.__objects = json.loads(FileStorage.__file_path)
