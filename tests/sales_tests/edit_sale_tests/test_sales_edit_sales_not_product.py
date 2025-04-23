import pytest
from unittest.mock import MagicMock
from support.verify import Verify

def test_sales_edit_sale_not_product():

    product_name_entry = MagicMock()
    product_name_entry.get.return_value = ""

    console_text = MagicMock()

    verify = Verify(console_text).verify_if_edit_sale_is_product_name("")

    console_text.delete.assert_called_once_with(0, 'end')
    console_text.insert.assert_called_once_with(0, "Preencha o campo 'Nome do Produto'.")
    
    assert verify is False