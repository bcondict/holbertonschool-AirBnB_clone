#!/usr/bin/python3
""""""


import json


class FileStorage():
    __file_path = "{}.json".format(__name__)
    __objects = {}

    def all(self):
        """ return the class attribute __object """
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects["{}{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        with open(self.__file_path, "w", encoding="UTF-8") as f:
            json.dump(self.__class__.__objecets, f)

    def reload(self):
        FileStorage.__objects = json.loads(FileStorage.__file_path)
