import pytest
from modules.database import DataBase

def test_database_connect():

    db = DataBase(":memory:")

    try:
        db.connect()

        assert db.connect() is not None
    finally:
        db.close_connection()