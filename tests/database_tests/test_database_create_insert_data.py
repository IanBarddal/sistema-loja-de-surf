import pytest
from modules.database import DataBase

def test_database_create_insert_data():

    command = "INSERT INTO Produtos ('Produto', 'Preço Unitário', 'Estoque', 'Data de Adição', 'Imagem') values (?, ?, ?, ?, ?)"
    parameters = ["Produto X", 200.00, 20, "10/04/2025 23:35", "teste.jpg"]

    database_test = DataBase(":memory:")

    database_test.connect()

    database_test.create_database()

    database_test.create(command, parameters)

    result = database_test.read("SELECT * FROM Produtos WHERE Produto = ?", ["Produto X"])

    database_test.close_connection()

    assert result != []
    assert result [0][1] == "Produto X"
    assert result [0][2] == 200.00
    assert result [0][3] == 20
    assert result [0][4] == "10/04/2025 23:35"
    assert result [0][5] == "teste.jpg"
    
