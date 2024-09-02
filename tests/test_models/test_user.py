#!/usr/bin/python3
"""
Test Module for User
"""

from models.user import User
from models.engine.file_storage import FileStorage
from datetime import datetime
from io import StringIO
import os
import uuid
import unittest

class TestUser(unittest.TestCase):
    """
    Tests the functionality of User
    """

    @classmethod
    def setUpClass(cls):
        """
        Run once before all tests
        """
        cls.path = FileStorage._FileStorage__file_path

    def test_init(self):
        """
        Tests initialization of User
        """
        b = User()
        self.assertIs(uuid.UUID(b.id).version, 4)
        self.assertEqual(b.created_at, b.updated_at)
        self.assertIsInstance(b.created_at, datetime)
        c = User(**b.to_dict())
        self.assertEqual(c.id, b.id)
        self.assertEqual(b.created_at, c.created_at)
        self.assertIsInstance(c.created_at, datetime)

    def test_str(self):
        """
        Tests __str__ function
        """
        b = User()
        s = StringIO()
        print(b, file= s, end="")
        self.assertEqual(s.getvalue(), f"[{b.__class__.__name__}] ({b.id}) {b.__dict__}")


    def test_save(self):
        """
        Tests save function
        """
        b = User()
        self.assertEqual(b.created_at, b.updated_at)
        b.save()
        self.assertNotEqual(b.created_at, b.updated_at)
        self.assertTrue(os.path.exists(self.path))

    def test_to_dict(self):
        """
        Tests to_dict function
        """
        b = User()
        b_dict = b.to_dict()
        self.assertIs(b_dict['__class__'], "User")
        self.assertIsInstance(b_dict["created_at"], str)
        self.assertIsInstance(b_dict["updated_at"], str)

    def test_run_all(self):
        """
        Runs instances as test
        """
        a = User()
        a.first_name = "Betty"
        a.last_name = "Bar"
        a.email = "airbnb@mail.com"
        a.password = "root"
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
