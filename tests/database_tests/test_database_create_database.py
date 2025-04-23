import pytest
from modules.database import DataBase

def test_create_database():
    test_database = DataBase(":memory:")
    
    test_database.connect()

    test_database.create_database()

    tables = test_database.read("SELECT name FROM sqlite_master WHERE type='table';")
    test_database.close_connection()

    table_names = [table[0] for table in tables]

    assert "Produtos" in table_names
    assert "Clientes" in table_names
    assert "Vendas" in table_names