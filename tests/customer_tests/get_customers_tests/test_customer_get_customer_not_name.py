import pytest
from unittest.mock import MagicMock
from support.verify import Verify

def test_customer_get_customer_not_name():

    name_entry = MagicMock()
    name_entry.get.return_value = ""

    console_text = MagicMock()

    verify = Verify(console_text).verify_if_get_customer_is_name("")

    console_text.delete.assert_called_once_with(0, 'end')
    console_text.insert.assert_called_once_with(0, "Campo 'Nome' não pode estar vazio.")
    
    assert verify is False