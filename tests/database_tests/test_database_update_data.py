import pytest
from modules.database import DataBase

def test_database_update_data():

    database = DataBase(":memory:")
    database.connect()

    database.create_database()

    command = "INSERT INTO Produtos ('Produto', 'Preço Unitário', 'Estoque', 'Data de Adição', 'Imagem') VALUES (?, ?, ?, ?, ?)"
    parameters = ["Produto X", 100.0, 20, "10/04/2025 20:00", "teste.jpg"]

    database.create(command, parameters)

    update_command = "UPDATE Produtos SET Estoque = Estoque + ? WHERE Produto = ?"
    update_parameters = [2, "Produto X"]

    database.update(update_command, update_parameters)

    result = database.read("SELECT * FROM Produtos")

    assert result != []
    assert result[0][3] == 22