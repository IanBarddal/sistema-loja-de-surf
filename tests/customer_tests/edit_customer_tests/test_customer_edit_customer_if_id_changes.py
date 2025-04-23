import pytest
from unittest.mock import MagicMock
from support.verify import Verify
from modules.database import DataBase
from modules.customers import Customer  # Certifique-se de que a classe Customer está importada corretamente
from tkinter import END

def test_edit_customer_id_changes():
    console_text = MagicMock()

    id_entry = MagicMock()
    id_entry.get.return_value = 1

    name_entry = MagicMock()
    name_entry.get.return_value = "João da Silva"

    database = DataBase(":memory:")
    database.create_database()

    # Inserir clientes com IDs diferentes
    database.create("INSERT INTO Clientes (ID, Nome, CPF, Telefone) VALUES (?, ?, ?, ?)", [1, "Carlos Gomes", "555.555.555-55", "48999999999"])
    database.create("INSERT INTO Clientes (ID, Nome, CPF, Telefone) VALUES (?, ?, ?, ?)", [2, "João da Silva", "777.777.777-77", "48999991111"])

    verify = Verify(console_text, database=database).verify_if_id_changes(1, "João da Silva")

    assert verify is False
    console_text.delete.assert_called_once_with(0, END)
    console_text.insert.assert_called_once_with(0, "Não foi possível alterar o ID.")

    database.close_connection()