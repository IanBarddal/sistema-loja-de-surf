import pytest
from unittest.mock import MagicMock
from support.verify import Verify

def test_products_create_product_stock_is_digit():

    stock_entry = MagicMock()
    stock_entry.get.return_value = "-2"

    console_text = MagicMock()

    verify = Verify(console_text).verify_if_create_product_stock_is_digit("2A")

    console_text.delete.assert_called_once_with(0, 'end')
    console_text.insert.assert_called_once_with(0, "Campo 'Estoque' só pode conter números maiores que zero.")
    
    assert verify is False