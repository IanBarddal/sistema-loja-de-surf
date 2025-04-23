import pytest
from unittest.mock import MagicMock
from support.verify import Verify

def test_sales_sell_if_not_cpf():

    cpf_entry = MagicMock()
    cpf_entry.get.return_value = ""

    console_text = MagicMock()

    verify = Verify(console_text).verify_if_sell_is_cpf("")

    console_text.delete.assert_called_once_with(0, 'end')
    console_text.insert.assert_called_once_with(0, "Preencha o campo 'CPF'.")
    
    assert verify is False