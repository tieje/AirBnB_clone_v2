#!/usr/bin/python3
"""Database storage engine tests."""
from models.engine.db_storage import DBStorage
import os
import unittest


class test_DBStorage(unittest.TestCase):
    """Database storage engine tests."""

    def setUp(self):
        """Set environment variables."""
        environment_variables = {
            'HBNB_MYSQL_USER': 'hbnb_dev',
            'HBNB_MYSQL_PWD': 'hbnb_dev_pwd',
            'HBNB_MYSQL_HOST': 'localhost',
            'HBNB_MYSQL_DB': 'hbnb_dev_db',
            'HBNB_TYPE_STORAGE': 'db'
        }
        os.environ.update(environment_variables)

    def test_DBStorage_all(self):
        """Test `DBStorage.all()`."""
        # Create new DBStorage
        db_storage_engine = DBStorage()

        # Storage engine has no session yet; call `reload()` to create one
        db_storage_engine.reload()

        # Call all() method
        all_return = db_storage_engine.all()
        self.assertIsInstance(all_return, dict)

if __name__ == "__main__":
    unittest.main()
