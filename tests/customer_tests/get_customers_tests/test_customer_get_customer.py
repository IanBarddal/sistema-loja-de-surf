import pytest
from modules.database import DataBase
from modules.customers import Customer
from unittest.mock import MagicMock

def test_customer_get_customer():

    id_entry = MagicMock()

    name_entry = MagicMock()
    name_entry.get.return_value = "Carlos Eduardo Gomes"

    cpf_entry = MagicMock()
    cpf_entry.get.return_value = "555.555.555-55"

    phone_entry = MagicMock()
    phone_entry.get.return_value = "48999999999"

    console_text = MagicMock()

    # Banco em memória e com tabelas criadas
    database = DataBase(":memory:")  # Banco de dados em memória
    database.create_database()  # Garante que as tabelas sejam criadas antes de qualquer operação

    # Cria o cliente e registra
    database.create("INSERT INTO Clientes (Nome, Cpf, Telefone) VALUES (?, ?, ?)", ["Carlos Eduardo Gomes", "555.555.555-55", "48999999999"])

    customer_data = database.read("SELECT * FROM Clientes WHERE CPF = ?", ["555.555.555-55"])[0]
    expected_console_text = (
        f"ID do Cliente: {customer_data[0]} | Nome do Cliente: {customer_data[1]} | CPF: {customer_data[2]} | Telefone: {customer_data[3]} | Data de Adesão: {customer_data[4]}"
    )

    customer = Customer(id_entry, name_entry, cpf_entry, phone_entry, console_text, database=database)
    customer.get_customer()

    console_text.delete.assert_called_once_with(0, 'end')
    console_text.insert.assert_called_once_with(0, expected_console_text)

    database.close_connection()