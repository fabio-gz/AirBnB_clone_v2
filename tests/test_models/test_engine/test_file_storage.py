#!/usr/bin/python3
"""test for file storage"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    '''this will test the FileStorage'''

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.user = User()
        cls.user.first_name = "Kev"
        cls.user.last_name = "Yo"
        cls.user.email = "1234@yahoo.com"
        cls.storage = FileStorage()

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.user

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_FileStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all(self):
        """tests if all works in File Storage"""
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_new(self):
        """test when new is created"""
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.id = 123455
        user.name = "Kevin"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])

    def test_reload_filestorage(self):
        """
        tests reload
        """
        self.storage.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, "file.json")
        with open(path, 'r') as f:
            lines = f.readlines()
        try:
            os.remove(path)
        except:
            pass
        self.storage.save()
        with open(path, 'r') as f:
            lines2 = f.readlines()
        self.assertEqual(lines, lines2)
        try:
            os.remove(path)
        except:
            pass
        with open(path, "w") as f:
            f.write("{}")
        with open(path, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)

    def test_delete_user(self):
        storage = FileStorage()
        obj = storage.all()
        user = User()
        key = user.__class__.__name__ + "." + str(user.id)
        storage.delete(user)
        obj2 = storage.all()
        self.assertNotEqual(obj[key], obj2[key])

    def test_delete_state(self):
        storage = FileStorage()
        obj = storage.all()
        state = State()
        key = state.__class__.__name__ + "." + str(state.id)
        storage.delete(state)
        obj2 = storage.all()
        self.assertNotEqual(obj[key], obj2[key])

    def test_delete_city(self):
        storage = FileStorage()
        obj = storage.all()
        city = City()
        key = city.__class__.__name__ + "." + str(city.id)
        storage.delete(city)
        obj2 = storage.all()
        self.assertNotEqual(obj[key], obj2[key])

    def test_delete_amenity(self):
        storage = FileStorage()
        obj = storage.all()
        amenity = Amenity()
        key = amenity.__class__.__name__ + "." + str(amenity.id)
        storage.delete(user)
        obj2 = storage.all()
        self.assertNotEqual(obj[key], obj2[key])

    def test_delete_review(self):
        storage = FileStorage()
        obj = storage.all()
        review = Review()
        key = review.__class__.__name__ + "." + str(Review.id)
        storage.delete(review)
        obj2 = storage.all()
        self.assertNotEqual(obj[key], obj2[key])

    def test_delete_place(self):
        storage = FileStorage()
        obj = storage.all()
        place = Place()
        key = place.__class__.__name__ + "." + str(place.id)
        storage.delete(place)
        obj2 = storage.all()
        self.assertNotEqual(obj[key], obj2[key])

if __name__ == "__main__":
    unittest.main()
