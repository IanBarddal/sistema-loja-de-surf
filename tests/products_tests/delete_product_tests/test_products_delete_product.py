from unittest.mock import MagicMock
import pytest
from modules.database import DataBase
from modules.products import Products

def test_products_delete_product():

    id_entry = MagicMock()

    amount_entry = MagicMock()

    name_entry = MagicMock()
    name_entry.get.return_value = "Prancha de Surf"

    price_entry = MagicMock()

    stock_entry = MagicMock()

    console_text = MagicMock()

    database = DataBase(":memory:")
    database.create_database()

    # Insere dois clientes manualmente
    database.create("INSERT INTO Produtos (Produto, 'Preço Unitário', Estoque) VALUES (?, ?, ?)",
                    ["Prancha de Surf", 2300.00, 20])
    
    product = Products(id_entry, name_entry, price_entry, stock_entry, amount_entry, console_text, database=database)
    product.delete_product()

    result = database.read("SELECT * FROM Produtos WHERE Produto = ?", ["Prancha de Surf"])

    for results in result:
        assert results[1] != "Prancha de Surf"
    
    console_text.delete.assert_called_once()
    console_text.insert.assert_called_with(0, "Produto deletado com sucesso.")

    database.close_connection()