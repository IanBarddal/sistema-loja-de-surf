import pytest
from modules.database import DataBase

def test_database_delete_data():

    database = DataBase(":memory:")
    database.connect()

    database.create_database()

    command = "INSERT INTO Produtos ('Produto', 'Preço Unitário', 'Estoque', 'Data de Adição', 'Imagem') VALUES (?, ?, ?, ?, ?)"
    parameters = ["Produto X", 100.0, 20, "10/04/2025 20:00", "teste.jpg"]

    database.create(command, parameters)

    database.delete("DELETE FROM Produtos WHERE Produto = ?", ["Produto X"])

    result = database.read("SELECT * FROM Produtos WHERE Produto = ?", ["Produto X"])

    assert result == []