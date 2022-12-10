#!/usr/bin/python3
"""Module for Filestorage class"""
import json
from models.base_model import BaseModel
from os import path

class FileStorage:
    """Class of file storage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return (FileStorage.__objects)

    def new(self, obj):
        """sets in __objects the object with key <obj class name>.id"""
        key = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(key, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()
            # Open the file and write to it
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump(obj_dict.f)   # Serialize python dictionary to json

    def reload(self):
        """Deserialize the JSON file to __objects"""
        if path.exists(FileStorage.__file_path):
            # Open the file and read from it
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    FileStorage.__objects[key] = \
                        eval(value['__class__'])(**value)
