import pytest
from unittest.mock import MagicMock
from support.verify import Verify

def test_sales_edit_sale_price_is_digit():

    price_entry = MagicMock()
    price_entry.get.return_value = "1A"

    console_text = MagicMock()

    verify = Verify(console_text).verify_if_edit_sale_price_is_digit("1A")

    console_text.delete.assert_called_once_with(0, 'end')
    console_text.insert.assert_called_once_with(0, "Coloque um preço válido para o produto.")
    
    assert verify is False