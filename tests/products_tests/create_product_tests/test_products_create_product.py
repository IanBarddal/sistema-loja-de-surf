import pytest
from modules.database import DataBase
from modules.products import Products
from unittest.mock import MagicMock, patch

@patch.object(Products, 'choose_image', return_value="teste.jpg")
def test_customer_create_product(mock_choose_image):

    id_entry = MagicMock()
    amount_entry = MagicMock()
    name_entry = MagicMock()
    name_entry.get.return_value = "Skate"
    price_entry = MagicMock()
    price_entry.get.return_value = "300"
    stock_entry = MagicMock()
    stock_entry.get.return_value = "20"
    console_text = MagicMock()

    database = DataBase(":memory:")
    database.create_database()

    product = Products(id_entry, name_entry, price_entry, stock_entry, amount_entry, console_text, database=database)

    product.create_product()

    result = database.read("SELECT * FROM Produtos WHERE Produto = ?", ["Skate"])
    database.close_connection()

    assert len(result) == 1
    assert result[0][1] == "Skate"
    assert result[0][2] == 300
    assert result[0][3] == 20
    assert result[0][5] == "teste.jpg"