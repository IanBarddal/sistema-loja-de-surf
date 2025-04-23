import pytest
from unittest.mock import MagicMock
from support.verify import Verify

def test_sales_delete_sale_not_id():

    sale_id_entry = MagicMock()
    sale_id_entry.get.return_value = ""

    console_text = MagicMock()

    verify = Verify(console_text).verify_delete_sale_not_id("")

    console_text.delete.assert_called_once_with(0, 'end')
    console_text.insert.assert_called_once_with(0, "Preencha o campo 'ID da Venda'.")
    
    assert verify is False