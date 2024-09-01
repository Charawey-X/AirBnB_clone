#!/usr/bin/python3
"""
Test Module for BaseModel
"""

from models.base_model import BaseModel
from datetime import datetime
from io import StringIO
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
        self.assertIsInstance(b.created_at, datetime)
        c = BaseModel(**b.to_dict())
        self.assertEqual(c.id, b.id)
        self.assertEqual(b.created_at, c.created_at)
        self.assertIsInstance(c.created_at, datetime)

    def test_str(self):
        b = BaseModel()
        s = StringIO()
        print(b, file= s, end="")
        self.assertEqual(s.getvalue(), f"[{b.__class__.__name__}] ({b.id}) {b.__dict__}]")


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
