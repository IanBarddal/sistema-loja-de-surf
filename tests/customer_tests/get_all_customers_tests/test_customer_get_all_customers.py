from unittest.mock import MagicMock, call
import pytest
from modules.database import DataBase
from modules.customers import Customer

def test_customer_get_all_customers():

    id_entry = MagicMock()

    name_entry = MagicMock()
    name_entry.get.return_value = "Carlos Eduardo Gomes"

    cpf_entry = MagicMock()
    cpf_entry.get.return_value = "555.555.555-55"

    phone_entry = MagicMock()
    phone_entry.get.return_value = "48999999999"

    console_text = MagicMock()

    database = DataBase(":memory:")
    database.create_database()

    # Insere dois clientes manualmente
    database.create("INSERT INTO Clientes (Nome, CPF, Telefone) VALUES (?, ?, ?)",
                    ["Carlos Eduardo Gomes", "555.555.555-55", "48999999999"])
    database.create("INSERT INTO Clientes (Nome, CPF, Telefone) VALUES (?, ?, ?)",
                    ["João da Silva", "222.222.222-22", "4838717711"])

    customer = Customer(id_entry, name_entry, cpf_entry, phone_entry, console_text, database=database)
    customer.get_all_customers()

    expected_calls = [
        call(0, "ID do Cliente: 2 | Nome do Cliente: João da Silva | CPF: 222.222.222-22 | Telefone: 4838717711 | Data de Adesão: None\n\n"),
        call(0, "ID do Cliente: 1 | Nome do Cliente: Carlos Eduardo Gomes | CPF: 555.555.555-55 | Telefone: 48999999999 | Data de Adesão: None\n\n"),
    ]

    console_text.delete.assert_called_once_with(0, 'end')
    console_text.insert.assert_has_calls(expected_calls, any_order=False)

    database.close_connection()