#!/usr/bin/python3
""" BaseModel """
import uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel:

    """ Class for base model where all others inherit from """
    def __init__(self, *args, **kwargs):
        """ base model constructor """

        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)
        
    def __str__(self):
        """ representation """

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)
    
    def save(self):
        """ Updates the instance updated_at with current datetime """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ create new dict for the current class """
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict

