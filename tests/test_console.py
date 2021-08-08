#!/usr/bin/python3
""" Test the console """
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.__init__ import storage
from console import HBNBCommand
from unittest.mock import patch
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State
from models.city import City
from models.user import User
from io import StringIO
import console
import unittest
import sys
import os

class TestConsole(unittest.TestCase):
    """ Test Console. """
    def setUp(self):
        """Set up """
        self.console_o = HBNBCommand()

    def tearDown(self):
        """clean up"""
        pass

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'for databases')
    def test_create(self):
        """test create"""
        with patch("sys.stdout", new=StringIO()) as out:
            self.console_o.onecmd("create User")
            lenn = len(out.getvalue())
            self.assertTrue(lenn > 0)
        with patch("sys.stdout", new=StringIO()) as out:
            self.console_o.onecmd("create Lauca")
            self.assertEqual("** class doesn't exist **\n", out.getvalue())
        with patch("sys.stdout", new=StringIO()) as out:
            self.console_o.onecmd("create")
            self.assertEqual("** class name missing **\n", out.getvalue())
        with patch("sys.stdout", new=StringIO()) as out:
            self.console_o.onecmd("all State")
            lenn = len(out.getvalue())
            self.assertTrue(lenn > 0)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'for file')
    def test_create(self):
        """test create"""
        with patch("sys.stdout", new=StringIO()) as out:
            self.console_o.onecmd("create User")
            lenn = len(out.getvalue())
            self.assertTrue(lenn > 0)
        with patch("sys.stdout", new=StringIO()) as out:
            self.console_o.onecmd("create Lauca")
            self.assertEqual("** class doesn't exist **\n", out.getvalue())
        with patch("sys.stdout", new=StringIO()) as out:
            self.console_o.onecmd("create")
            self.assertEqual("** class name missing **\n", out.getvalue())
        with patch("sys.stdout", new=StringIO()) as out:
            self.console_o.onecmd("all State")
            lenn = len(out.getvalue())
            self.assertTrue(lenn > 0)


if __name__ == "__main__":
    unittest.main()

# python3 -m unittest discover tests
# python3 -m unittest tests/test_models/test_base_model.py