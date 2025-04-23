from unittest.mock import MagicMock, call
import pytest
from modules.database import DataBase
from modules.products import Products

def test_products_get_product():

    id_entry = MagicMock()

    amount_entry = MagicMock()

    name_entry = MagicMock()
    name_entry.get.return_value = "Prancha de Surf"

    price_entry = MagicMock()
    price_entry.get.return_value = 2300

    stock_entry = MagicMock()
    stock_entry.get.return_value = 20

    console_text = MagicMock()

    database = DataBase(":memory:")
    database.create_database()

    database.create("INSERT INTO Produtos (Produto, 'Preço Unitário', Estoque, 'Data de Adição', Imagem) VALUES (?, ?, ?, ?, ?)",
                    ["Prancha de Surf", 2300, 20, "12/04/2025 23:35", "teste.jpg"])

    product = Products(id_entry, name_entry, price_entry, stock_entry, amount_entry, console_text, database=database)
    product.get_product()

    result = database.read("SELECT * FROM Produtos WHERE Produto = ?", ["Prancha de Surf"])

    assert result != []
    assert result[0][1] == "Prancha de Surf"
    assert result[0][2] == 2300.00
    assert result[0][3] == 20
    assert result[0][4] == "12/04/2025 23:35"
    assert result[0][5] == "teste.jpg"

    print(console_text.insert.call_args_list)

    console_text.delete.assert_called_with(0, "end")
    console_text.insert.assert_called_with(0, "ID do Produto: 1 | Nome do Produto: Prancha de Surf | Preço Unitário: R$ 2300,00 | Quantidade em Estoque: 20 | Data de Adição: 12/04/2025 23:35\n\n")

    database.close_connection()