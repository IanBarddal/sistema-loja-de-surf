from unittest.mock import MagicMock, call
import pytest
from modules.database import DataBase
from modules.sales import Sales

def test_sales_get_sale():

    id_entry = MagicMock()
    id_entry.get.return_value = 1

    product_name_entry = MagicMock()
    product_name_entry.get.return_value = "Prancha de Surf"

    customer_name_entry = MagicMock()
    customer_name_entry.get.return_value = "João da Silva"

    cpf_entry = MagicMock()
    cpf_entry.get.return_value = "777.777.777-77"

    price_entry = MagicMock()
    price_entry.get.return_value = 1500

    amount_entry = MagicMock()
    amount_entry.get.return_value = 1

    new_amount_entry = MagicMock()
    difference_entry = MagicMock()
    console_text = MagicMock()

    database = DataBase(":memory:")
    database.create_database()

    database.create("INSERT INTO Vendas ('Cliente', 'CPF', 'Produto', 'Quantidade Vendida', 'Valor Total') VALUES (?, ?, ?, ?, ?)",
                    ["João da Silva", "777.777.777-77", "Prancha de Surf", 1, 1500.00])

    sales = Sales(id_entry, product_name_entry, customer_name_entry, cpf_entry, amount_entry, price_entry, new_amount_entry, difference_entry, console_text, database=database)
    sales.get_sale()

    result = database.read("SELECT * FROM Vendas WHERE ID = ?", [1])

    assert result != []
    assert result[0][1] == "João da Silva"
    assert result[0][2] == "777.777.777-77"
    assert result[0][3] == "Prancha de Surf"
    assert result[0][4] == 1
    assert result[0][5] == 1500

    console_text.delete.assert_called_with(0, "end")
    console_text.insert.assert_called_with(0, "ID da Venda: 1 | Cliente: João da Silva | CPF: 777.777.777-77 | Produto: Prancha de Surf | Quantidade Vendida: 1 | Valor Total: R$ 1500,00 | Data da Venda: None")

    database.close_connection()