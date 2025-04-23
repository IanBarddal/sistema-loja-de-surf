import pytest
from unittest.mock import MagicMock
from support.verify import Verify

def test_sales_edit_sale_not_new_amount():

    new_amount_entry = MagicMock()
    new_amount_entry.get.return_value = ""

    console_text = MagicMock()

    verify = Verify(console_text).verify_if_edit_sale_is_new_amount("")

    console_text.delete.assert_called_once_with(0, 'end')
    console_text.insert.assert_called_once_with(0, "Coloque um valor válido para a quantidade.")
    
    assert verify is False