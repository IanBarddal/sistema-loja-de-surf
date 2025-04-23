from unittest.mock import MagicMock, call
import pytest
from modules.database import DataBase
from modules.products import Products

def test_products_get_all_products():

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

    # Insere dois clientes manualmente
    database.create("INSERT INTO Produtos (Produto, 'Preço Unitário', Estoque) VALUES (?, ?, ?)",
                    ["Prancha de Surf", 2300, 20])
    database.create("INSERT INTO Produtos (Produto, 'Preço Unitário', Estoque) VALUES (?, ?, ?)",
                    ["Quilhas", 250, 20])

    product = Products(id_entry, name_entry, price_entry, stock_entry, amount_entry, console_text, database=database)
    product.get_all_products()

    expected_calls = [
        call(0, "ID do Produto: 2 | Nome do Produto: Quilhas | Preço Unitário: R$ 250,00 | Quantidade em Estoque: 20 | Data de Adição: None\n\n"),
        call(0, "ID do Produto: 1 | Nome do Produto: Prancha de Surf | Preço Unitário: R$ 2300,00 | Quantidade em Estoque: 20 | Data de Adição: None\n\n"),
    ]

    console_text.delete.assert_called_once_with(0, 'end')
    console_text.insert.assert_has_calls(expected_calls, any_order=False)

    database.close_connection()