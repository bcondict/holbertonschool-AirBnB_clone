#!/usr/bin/python3
""""""


import json


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return the class attribute __object """
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects["{}{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        with open(FileStorage.__file_path, "w", encoding="UTF-8") as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        try:
            FileStorage.__objects = json.loads(FileStorage.__file_path)

        except Exception:
            return
