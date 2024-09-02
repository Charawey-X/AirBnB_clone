#!/usr/bin/python3

from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage


classes = {"Amenity": Amenity, "BaseModel": BaseModel,  "City": City, "Place": Place, "Review": Review, "State": State, "User": User}

storage = FileStorage()
storage.reload()

