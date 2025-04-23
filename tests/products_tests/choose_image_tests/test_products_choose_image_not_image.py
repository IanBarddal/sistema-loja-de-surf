import pytest
from unittest.mock import MagicMock, patch
from modules.products import Products
from modules.database import DataBase

def test_products_choose_image_not_image():

    id_entry = MagicMock()

    amount_entry = MagicMock()

    name_entry = MagicMock()
    name_entry.get.return_value = "Prancha de Surf"

    price_entry = MagicMock()
    price_entry.get.return_value = 2300.00

    stock_entry = MagicMock()
    stock_entry.get.return_value = 20

    image_entry = MagicMock()
    image_entry.get.return_value = ""

    console_text = MagicMock()

    database = DataBase(":memory:")
    database.create_database()

    product = Products(id_entry, name_entry, price_entry, stock_entry, amount_entry, console_text, database=database)

    with patch("modules.products.filedialog.askopenfilename", return_value=""):
        result = product.choose_image()

    assert result is None

    console_text.delete.assert_called_once_with(0, "end")
    console_text.insert.assert_called_once_with(0, "Selecione uma imagem para o produto.")

    database.close_connection()