import pytest
from unittest.mock import MagicMock
from modules.database import DataBase
from modules.sales import Sales

def test_products_update_stock():

    sale_id_entry = MagicMock()

    amount_entry = MagicMock()
    amount_entry.get.return_value = "1"

    product_name_entry = MagicMock()
    product_name_entry.get.return_value = "Prancha de Surf"

    customer_name_entry = MagicMock()
    customer_name_entry.get.return_value = "João da Silva"

    cpf_entry = MagicMock()
    cpf_entry.get.return_value = "555.555.555-55"

    price_entry = MagicMock()
    price_entry.get.return_value = "2300"

    new_quantity_entry = MagicMock()

    difference_entry = MagicMock()

    console_text = MagicMock()

    database = DataBase(":memory:")
    database.create_database()

    database.create("INSERT INTO Produtos (ID, Produto, 'Preço Unitário', Estoque) VALUES (?, ?, ?, ?)", [1, "Prancha de Surf", 2300, 20])
    
    database.create("INSERT INTO Clientes (Nome, CPF, Telefone) VALUES (?, ?, ?)", ["João da Silva", "555.555.555-55", "48999999999"])
    
    database.create("INSERT INTO Vendas (Cliente, CPF, Produto, 'Quantidade Vendida', 'Valor Total') VALUES (?, ?, ?, ?, ?)", ["João da Silva", "555.555.555-55", "Prancha de Surf", 1, 2300.00])

    sale = Sales(sale_id_entry, product_name_entry, customer_name_entry, cpf_entry, amount_entry, price_entry, new_quantity_entry, difference_entry, console_text, database=database)
    sale.sell()
    
    result = database.read("SELECT * FROM Produtos WHERE Produto = ?", ["Prancha de Surf"])
        
    assert result[0][3] == 19

    database.close_connection()