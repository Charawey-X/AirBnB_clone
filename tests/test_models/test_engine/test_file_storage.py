#!/usr/bin/python3

"""
Test Module for FileStorage
"""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest

class TestFileStorage(unittest.TestCase):
    """
    Tests the functionality of FileStorage
    """

    f = FileStorage()

    def test_all_and_new(self):
        self.assertTrue(len(self.f.all()) == 0)
        b = BaseModel()
        self.assertIn(f"{b.__class__.__name__}.{b.id}", self.f.all().keys())
