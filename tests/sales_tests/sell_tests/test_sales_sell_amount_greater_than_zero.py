import pytest
from unittest.mock import MagicMock
from support.verify import Verify

def test_sales_sell_amount_greater_than_zero():

    amount_entry = MagicMock()
    amount_entry.get.return_value = 0

    console_text = MagicMock()

    verify = Verify(console_text).verify_if_sell_amount_is_greater_than_zero(0)

    console_text.delete.assert_called_once_with(0, 'end')
    console_text.insert.assert_called_once_with(0, "Campo 'Quantidade' só aceita números maiores que zero.")
    
    assert verify is False