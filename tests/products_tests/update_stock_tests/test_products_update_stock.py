import pytest
from unittest.mock import MagicMock
from modules.database import DataBase
from modules.products import Products

def test_products_update_stock():

    id_entry = MagicMock()
    id_entry.get.return_value = 1

    amount_entry = MagicMock()
    amount_entry.get.return_value = 2

    name_entry = MagicMock()
    name_entry.get.return_value = "Prancha de Surf"

    price_entry = MagicMock()

    stock_entry = MagicMock()

    console_text = MagicMock()

    database = DataBase(":memory:")
    database.create_database()
    
    database.create("INSERT INTO Produtos (ID, Produto, 'Preço Unitário', Estoque) VALUES (?, ?, ?, ?)",
                    [1, "Prancha de Surf", 2300.00, 20])
    
    product = Products(id_entry, name_entry, price_entry, stock_entry, amount_entry, console_text, database=database)
    product.update_stock()

    result = database.read("SELECT * FROM Produtos WHERE Produto = ?", ["Prancha de Surf"])
        
    assert result[0][3] == 22
    
    console_text.delete.assert_called_once()
    console_text.insert.assert_called_with(0, "Estoque atualizado com sucesso.")

    database.close_connection()