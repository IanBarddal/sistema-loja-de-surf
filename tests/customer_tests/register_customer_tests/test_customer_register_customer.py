import pytest
from modules.database import DataBase
from modules.customers import Customer
from unittest.mock import MagicMock

def test_customer_register_customer():

    id_entry = MagicMock()

    name_entry = MagicMock()
    name_entry.get.return_value = "João da Silva"

    cpf_entry = MagicMock()
    cpf_entry.get.return_value = "555.555.555-55"

    phone_entry = MagicMock()
    phone_entry.get.return_value = "48999999999"

    console_text = MagicMock()

    # Banco em memória e com tabelas criadas
    database = DataBase(":memory:")  # Banco de dados em memória
    database.create_database()  # Garante que as tabelas sejam criadas antes de qualquer operação

    # Cria o cliente e registra
    customer = Customer(id_entry, name_entry, cpf_entry, phone_entry, console_text, database=database)
    customer.register_customer()

    result = database.read("SELECT * FROM Clientes WHERE Nome = ?", ["João da Silva"])

    database.close_connection()

    assert len(result) == 1
    assert result[0][1] == "João da Silva"