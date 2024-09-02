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
        try:
            os.remove(cls.path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """
        Tests all function
        """
        self.assertTrue(len(self.objects) == 0)
        a = BaseModel()
        self.assertIn(f"{a.__class__.__name__}.{a.id}", self.storage.all().keys())

    def test_new(self):
        """
        Tests new function
        """
        b_dict = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': '2017-09-28T21:03:54.052298',
                  '__class__': 'BaseModel', 'my_number': 89, 'updated_at': '2017-09-28T21:03:54.052302',
                  'name': 'My_First_Model'}
        b = BaseModel(**b_dict)
        self.assertNotIn(f"{b.__class__.__name__}.{b.id}", self.objects.keys())


    def test_save(self):
        """
        Tests save function
        """
        c = BaseModel()
        c.save()
        self.assertTrue(os.path.isfile(self.path))
        #self.assertIn(f"{c.__class__.__name__}.{c.id}", self.objects.keys())

    def test_reload(self):
        """
        Tests reload function
        """
        d = BaseModel()
        d.save()
        expected = len(self.objects)
        actual = {}
        self.assertTrue(os.path.exists(self.path))
        with open(self.path, mode = 'r') as f:
            actual = json.load(f)
        print(actual)
        FileStorage._FileStorage__objects = {}
        self.storage.reload()
        self.assertEqual(expected, len(actual))
        self.assertEqual(len(actual), len(FileStorage._FileStorage__objects))

    @classmethod
    def tearDownClass(cls):
        """
        Run after all tests are done
        """
        try:
            os.remove(cls.path)
        except (FileNotFoundError):
            pass
