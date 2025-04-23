import pytest
from modules.database import DataBase

def test_database_close_connection():

    memory_db = DataBase(":memory:")

    memory_db.connect()

    memory_db.close_connection()
        
    assert memory_db.connection is None