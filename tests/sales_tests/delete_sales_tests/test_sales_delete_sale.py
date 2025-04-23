from unittest.mock import MagicMock
import pytest
from modules.database import DataBase
from modules.sales import Sales

def test_sales_delete_sale():

    id_entry = MagicMock()
    id_entry.get.return_value = 1

    amount_entry = MagicMock()

    product_name_entry = MagicMock()

    customer_name_entry = MagicMock()

    price_entry = MagicMock()

    cpf_entry = MagicMock()

    difference_entry = MagicMock()

    new_quantity_entry = MagicMock()

    console_text = MagicMock()

    database = DataBase(":memory:")
    database.create_database()

    database.create("INSERT INTO Produtos (ID, Produto, 'Preço Unitário', Estoque) VALUES (?, ?, ?, ?)", [1, "Prancha de Surf", 2300, 20])

    database.create("INSERT INTO Clientes (Nome, CPF, Telefone) VALUES (?, ?, ?)", ["João da Silva", "555.555.555-55", "48999999999"])
    
    database.create("INSERT INTO Vendas (ID, Cliente, CPF, Produto, 'Quantidade Vendida', 'Valor Total') VALUES (?, ?, ?, ?, ?, ?)", [1, "João da Silva", "555.555.555-55", "Prancha de Surf", 2, 2300.00])
    
    sale = Sales(id_entry, product_name_entry, customer_name_entry, cpf_entry, amount_entry, price_entry, new_quantity_entry, difference_entry, console_text, database=database)
    sale.delete_sale()

    result = database.read("SELECT * FROM Vendas WHERE ID = ?", [1])

    assert result == []

    database.close_connection()