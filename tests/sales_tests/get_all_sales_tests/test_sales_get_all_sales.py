from unittest.mock import MagicMock, call
import pytest
from modules.database import DataBase
from modules.sales import Sales

def test_sales_get_all_sales():

    id_entry = MagicMock()
    product_name_entry = MagicMock()
    customer_name_entry = MagicMock()
    cpf_entry = MagicMock()
    price_entry = MagicMock()
    amount_entry = MagicMock()
    new_amount_entry = MagicMock()
    difference_entry = MagicMock()
    console_text = MagicMock()

    database = DataBase(":memory:")
    database.create_database()

    # Insere dois clientes manualmente
    database.create("INSERT INTO Vendas ('Cliente', 'CPF', 'Produto', 'Quantidade Vendida', 'Valor Total') VALUES (?, ?, ?, ?, ?)",
                    ["João da Silva", "777.777.777-77", "Prancha de Surf", 1, 1500])
    database.create("INSERT INTO Vendas ('Cliente', 'CPF', 'Produto', 'Quantidade Vendida', 'Valor Total') VALUES (?, ?, ?, ?, ?)",
                    ["Carlos Gomes", "222.222.222-22", "Skate", 1, 250.00])

    sales = Sales(id_entry, product_name_entry, customer_name_entry, cpf_entry, amount_entry, price_entry, new_amount_entry, difference_entry, console_text, database=database)
    sales.get_all_sales()

    expected_calls = [ 
    call(0,"ID da Venda: 2 | Cliente: Carlos Gomes | CPF: 222.222.222-22 | Produto: Skate | Quantidade Vendida: 1 | Valor Total: R$ 250,00 | Data da Venda: None\n\n"),
    call(0,"ID da Venda: 1 | Cliente: João da Silva | CPF: 777.777.777-77 | Produto: Prancha de Surf | Quantidade Vendida: 1 | Valor Total: R$ 1500,00 | Data da Venda: None\n\n")
    ]

    console_text.delete.assert_called_once_with(0, 'end')
    console_text.insert.assert_has_calls(expected_calls, any_order=False)

    database.close_connection()