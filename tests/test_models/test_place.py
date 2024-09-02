#!/usr/bin/python3
"""
Test Module for Place
"""

from models.place import Place
from models.engine.file_storage import FileStorage
from datetime import datetime
from io import StringIO
import os
import uuid
import unittest

class TestPlace(unittest.TestCase):
    """
    Tests the functionality of Place
    """

    @classmethod
    def setUpClass(cls):
        """
        Run once before all tests
        """
        cls.path = FileStorage._FileStorage__file_path

    def test_init(self):
        """
        Tests initialization of Place
        """
        b = Place()
        self.assertIs(uuid.UUID(b.id).version, 4)
        self.assertEqual(b.created_at, b.updated_at)
        self.assertIsInstance(b.created_at, datetime)
        c = Place(**b.to_dict())
        self.assertEqual(c.id, b.id)
        self.assertEqual(b.created_at, c.created_at)
        self.assertIsInstance(c.created_at, datetime)
        self.assertIs(c.city_id, "")
        self.assertEqual(c.name, c.description)
        self.assertTrue(len(c.amenity_ids) == 0)
        self.assertEqual(c.price_by_night, 0)
        self.assertIs(c.user_id, "")
        self.assertEqual(c.number_rooms, 0)
        self.assertEqual(c.max_guest, 0)
        self.assertEqual(c.number_bathrooms, 0)
        self.assertIsInstance(c.longitude, float)
        self.assertIsInstance(c.latitude, float)




    def test_str(self):
        """
        Tests __str__ function
        """
        b = Place()
        s = StringIO()
        print(b, file= s, end="")
        self.assertEqual(s.getvalue(), f"[{b.__class__.__name__}] ({b.id}) {b.__dict__}")


    def test_save(self):
        """
        Tests save function
        """
        b = Place()
        self.assertEqual(b.created_at, b.updated_at)
        b.save()
        self.assertNotEqual(b.created_at, b.updated_at)
        self.assertTrue(os.path.exists(self.path))

    def test_to_dict(self):
        """
        Tests to_dict function
        """
        b = Place()
        b_dict = b.to_dict()
        self.assertIs(b_dict['__class__'], "Place")
        self.assertIsInstance(b_dict["created_at"], str)
        self.assertIsInstance(b_dict["updated_at"], str)

    @classmethod
    def tearDownClass(cls):
        """
        Run after all tests are done
        """
        try:
            os.remove(cls.path)
        except (FileNotFoundError):
            pass
