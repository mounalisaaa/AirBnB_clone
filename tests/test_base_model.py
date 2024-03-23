#!/usr/bin/python3
"""
Unittest for BaseModel
"""
import uuid
from datetime import datetime
import sys
import os
import unittest
import json

captured_output = StringIO()
sys.stdout = captured_output
current_dir = os.path.dirname(os.path.realpath(__file__))
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))