import pytest
from modules.database import DataBase
from modules.customers import Customer
from unittest.mock import MagicMock

def test_customer_edit_customer():

    id_entry = MagicMock()
    id_entry.get.return_value = 2

    name_entry = MagicMock()
    name_entry.get.return_value = "Carlos Eduardo Gomes"

    cpf_entry = MagicMock()
    cpf_entry.get.return_value = "555.555.555-55"

    phone_entry = MagicMock()
    phone_entry.get.return_value = "48999999999"

    console_text = MagicMock()

    database = DataBase(":memory:")  # Banco de dados em memória
    database.create_database()

    database.create("INSERT INTO Clientes (ID, Nome, Cpf, Telefone) VALUES (?, ?, ?, ?)", [2, "João da Silva", "555.555.555-55", "48999999999"])

    customer = Customer(id_entry, name_entry, cpf_entry, phone_entry, console_text, database=database)
    customer.edit_customer()

    result = database.read("SELECT * FROM Clientes WHERE ID = ?", [2])

    assert len(result) == 1
    assert result[0][1] == "Carlos Eduardo Gomes"

    database.close_connection()