#!/usr/bin/python3
"""
Test Module for BaseModel
"""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
from io import StringIO
import os
import uuid
import unittest

class TestBaseModel(unittest.TestCase):
    """
    Tests the functionality of BaseModel
    """

    @classmethod
    def setUpClass(cls):
        """
        Run once before all tests
        """
        cls.path = FileStorage._FileStorage__file_path

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
        self.assertTrue(os.path.exists(self.path))

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

    @classmethod
    def tearDownClass(cls):
        """
        Run after all tests are done
        """
        try:
            os.remove(cls.path)
        except (FileNotFoundError):
            pass
