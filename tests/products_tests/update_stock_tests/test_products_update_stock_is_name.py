import pytest
from unittest.mock import MagicMock
from support.verify import Verify

def test_products_update_stock_is_name():

    name_entry = MagicMock()
    name_entry.get.return_value = ""

    console_text = MagicMock()

    verify = Verify(console_text).verify_if_update_stock_is_name("")

    console_text.delete.assert_called_once_with(0, 'end')
    console_text.insert.assert_called_once_with(0, "Campo 'Nome do Produto' não pode estar vazio.")
    
    assert verify is False