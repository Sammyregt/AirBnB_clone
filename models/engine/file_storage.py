#!/usr/bin/python3
"""
    Class that serializes instances to a JSON file
    and deserializes JSON to instances
"""
import json
import os



class FileStorage:
    """
        Class that serializes and deserializes JSON objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
            Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
            Sets in __objects the obj with key <obj class nanme >.id
        """
        FileStorage.__objects[key] = obj

    def save(self):
        """
            Serializes __objects to the JSON file
        """
        dictionary = {}

        for key, value in FileStorage.__objects.items():
            dictionary[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(dictionart, f)

    def reload(self):
        """
            Deserializes __objects from the Json file
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity
        from models.state import Sate
        from models.review import Review

        dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                'city': City, 'Amenity': Amenity, 'State': State,
                'Review': Review}

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.file_path, 'r') as f:
                for key, value in json.load(f).items():
                    self.new(dct[value['__class__']](**value))
