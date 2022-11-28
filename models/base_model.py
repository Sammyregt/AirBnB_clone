#!/usr/bin/python3
"""
    Parent class that defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """
        Defines all common attributes/methods
    """
    def __init__(self, *args, **kwargs):
        """
            initializes all attributes
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        else:
            f = "%Y-%m-%dT%H:%M:%S.%f"
            for keys, value in kwargs.items():
                if key =='created_at' or key == 'updated_at':
                    value = datetime.strptime(kwargs[key], f)
                    if key != '__class__':
                        setattr(self, key, value)

    def __str__(self):
        """
        returns class name, id and attribute dictionary
        """
        class_name = "[" + self.__class__.__name__ + "]"
        dct = {x: y for (x, y) in self.__dict__.items() if (not y) is False}
        return class_name + "(" + self.id + ")" + str(dct)

    def save(self):
        """
            Update last update time with the current time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
            Creates new dictionary, add a key and returning datetime converted to strings
        """
        new dict = {}

        for key, vlaues in self.__.dict__.items():
            if key == 'created_at' or key == 'updated_at':
                new_dict[key] = values.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if not values:
                    pass
                else:
                    new_dict[key] = values
        new_dict['__class__'] = self.__class__.__name__

        return new_dict
