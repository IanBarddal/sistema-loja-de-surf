import pytest
from unittest.mock import MagicMock
from support.verify import Verify

def test_sales_edit_sale_price_is_greater_than_zero():

    price_entry = MagicMock()
    price_entry.get.return_value = "0"

    console_text = MagicMock()

    verify = Verify(console_text).verify_if_edit_sale_price_is_greater_than_zero("0")

    console_text.delete.assert_called_once_with(0, 'end')
    console_text.insert.assert_called_once_with(0, "'Preço Unitário' não poder ser menor ou igual a zero.")
    
    assert verify is False