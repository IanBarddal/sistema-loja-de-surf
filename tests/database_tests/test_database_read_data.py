import pytest
from modules.database import DataBase

def test_database_read_data():

    database = DataBase(":memory:")
    database.connect()

    database.create_database()

    command = "INSERT INTO Produtos ('Produto', 'Preço Unitário', 'Estoque', 'Data de Adição', 'Imagem') VALUES (?, ?, ?, ?, ?)"
    parameters = ["Produto X", 100.0, 20, "10/04/2025 20:00", "teste.jpg"]

    database.create(command, parameters)

    read_command = "SELECT * FROM Produtos WHERE Produto = ?"
    read_parameters = ["Produto X"]

    result = database.read(read_command, read_parameters)

    assert result != []
    assert result[0][1] == "Produto X"