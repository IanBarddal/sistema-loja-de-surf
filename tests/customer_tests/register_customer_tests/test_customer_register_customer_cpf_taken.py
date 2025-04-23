import pytest
from modules.database import DataBase

def test_customer_register_cpf_taken():

    database = DataBase(":memory:")

    database.connect()

    database.create_database()

    command = "INSERT INTO Clientes ('Nome', 'CPF', 'Telefone', 'Data de Adesão') values (?, ?, ?, ?)"
    parameters = ["João da Silva", "222.222.222-22", "11999999999", "10/03/2025 23:35"]

    database.create(command, parameters)

    name_check = database.read("SELECT * FROM Clientes WHERE CPF = ?", ["222.222.222-22"])

    assert len(name_check) == 1

    if not name_check:
        result = database.create(command, ["José Moreira", "222.222.222-22", "11888888888", "11/03/2025 22:20"])
    else:
        result = None

    all_customers_comparison = database.read("SELECT * FROM Clientes WHERE CPF = ?", ["222.222.222-22"])

    database.close_connection()

    assert len(all_customers_comparison) == 1

    assert result is None