#!/usr/bin/python3
"""
Test Module for BaseModel
"""

from models.base_model import BaseModel
import datetime
import uuid
import unittest

class TestBaseModel(unittest.TestCase):
    """
    Tests the functionality of BaseModel
    """
    def test_init(self):
        b = BaseModel()
        self.assertIs(uuid.UUID(b.id).version, 4)
        self.assertEqual(b.created_at, b.updated_at)
        self.assertIsInstance(b.created_at, datetime.datetime)

    def test_save(self):
        b = BaseModel()
        self.assertEqual(b.created_at, b.updated_at)
        b.save()
        self.assertNotEqual(b.created_at, b.updated_at)

    def test_to_dict(self):
        b = BaseModel()
        b_dict = b.to_dict()
        self.assertIs(b_dict['__class__'], "BaseModel")
        self.assertIsInstance(b_dict["created_at"], str)
        self.assertIsInstance(b_dict["updated_at"], str)

    def test_run_all(self):
        a = BaseModel()
        a.name = "My First Model"
        a.my_number = 89
        print(a)
        a.save()
        print(a)
        a_json = a.to_dict()
        print(a_json)
