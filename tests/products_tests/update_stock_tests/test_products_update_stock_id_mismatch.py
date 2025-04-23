from unittest.mock import MagicMock
import pytest
from modules.database import DataBase
from modules.products import Products

def test_products_update_stock_id_mismatch():

    id_entry = MagicMock()
    id_entry.get.return_value = 2

    amount_entry = MagicMock()

    name_entry = MagicMock()
    name_entry.get.return_value = "Prancha de Surf"

    price_entry = MagicMock()

    stock_entry = MagicMock()
    stock_entry.get.return_value = 2

    console_text = MagicMock()

    database = DataBase(":memory:")
    database.create_database()

    # Insere dois clientes manualmente
    database.create("INSERT INTO Produtos (ID, Produto, 'Preço Unitário', Estoque) VALUES (?, ?, ?, ?)",
                    [1, "Prancha de Surf", 2300.00, 20])
    database.create("INSERT INTO Produtos (ID, Produto, 'Preço Unitário', Estoque) VALUES (?, ?, ?, ?)",
                    [2, "Skate", 250.00, 20])
    
    product = Products(id_entry, name_entry, price_entry, stock_entry, amount_entry, console_text, database=database)
    product.update_stock()

    result = database.read("SELECT * FROM Produtos WHERE ID = ?", [2])
        
    assert name_entry.get.return_value != result[0][1]
    
    console_text.delete.assert_called_once()
    console_text.insert.assert_called_with(0, "Produto não casa com o ID.")

    database.close_connection()