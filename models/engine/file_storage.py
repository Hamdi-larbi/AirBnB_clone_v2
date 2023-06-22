#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of a cls models currently in storage"""
        if not cls:
            return FileStorage.__objects
        temp = {}
        for key, value in self.__objects.items():
            if key[1:key.find(']')] == cls:
                temp[key] = value
        return temp

    def new(self, obj):
        """Adds new object to storage dictionary"""
        FileStorage.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        import models

        classes = {
                    'BaseModel': models.BaseModel, 'User': models.User, 'Place': models.Place,
                    'State': models.State, 'City': models.City, 'Amenity': models.Amenity,
                    'Review': models.Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.__objects[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside - if obj is
        equal to None, the method should not do anything"""
        if obj != None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]
