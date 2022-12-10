#!/usr/bin/env python3
"""Module of BaseModel class"""
from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """class of BaseModel"""
    def __init__(self, *args, **kwargs):
        """Initialization of class attributes"""
        if kwargs:  # Perform an action when key words are entered
            for key, value in kwargs.items():   # Accepting dictionary objects
                if key == "__class__":   # Class objects defined in console.py
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def __str__(self):
        """Printing format of the output
        __class__.__name__ used to get the class name 
        of the object being retrieved
        """
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        # Saving output to dictionary objects
        new_dict = self.__dict__.copy() # makes a copy of the output
        new_dict['__class__'] = __class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict