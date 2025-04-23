import pytest
from unittest.mock import MagicMock
from support.verify import Verify

def test_customer_register_not_telephone():

    phone_entry = MagicMock()
    phone_entry.get.return_value = ""

    console_text = MagicMock()

    verify = Verify(console_text).verify_if_is_telephone("")

    console_text.delete.assert_called_once_with(0, 'end')
    console_text.insert.assert_called_once_with(0, "Campo 'Telefone' não pode estar vazio.")
    
    assert verify is False