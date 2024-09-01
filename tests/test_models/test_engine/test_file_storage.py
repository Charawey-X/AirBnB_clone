#!/usr/bin/python3

"""
Test Module for FileStorage
"""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json
import os.path
import unittest

class TestFileStorage(unittest.TestCase):
    """
    Tests the functionality of FileStorage
    """

    @classmethod
    def setUpClass(cls):
        """
        Run once before all tests
        """
        cls.storage = FileStorage()
        cls.objects = FileStorage._FileStorage__objects
        cls.path = FileStorage._FileStorage__file_path

    def test_all(self):
        self.assertTrue(len(self.objects) == 0)
        a = BaseModel()
        self.assertIn(f"{a.__class__.__name__}.{a.id}", self.storage.all().keys())

    def test_new(self):
        b_dict = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': '2017-09-28T21:03:54.052298',
                  '__class__': 'BaseModel', 'my_number': 89, 'updated_at': '2017-09-28T21:03:54.052302',
                  'name': 'My_First_Model'}
        b = BaseModel(**b_dict)
        self.assertNotIn(f"{b.__class__.__name__}.{b.id}", self.objects.keys())


    def test_save(self):
        c = BaseModel()
        c.save()
        self.assertTrue(os.path.isfile(self.path))
        self.assertIn(f"{c.__class__.__name__}.{c.id}", self.objects.keys())

    def test_reload(self):
        d = BaseModel()
        d.save()
        self.assertTrue(os.path.exists(self.path))
        self.storage.reload()
        self.assertIn(f"{d.__class__.__name__}.{d.id}", self.objects.keys())
        print(len(self.objects))

    @classmethod
    def tearDownClass(cls):
        """
        Run after all tests are done
        """
        try:
            os.remove(cls.path)
        except (FileNotFoundError):
            pass
