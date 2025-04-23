import pytest
from unittest.mock import MagicMock
from support.verify import Verify

def test_customer_edit_telephone_not_digit():

    phone_entry = MagicMock()
    phone_entry.get.return_value = "489999999AA"

    console_text = MagicMock()

    verify = Verify(console_text).verify_if_edit_telephone_is_digit("489999999AA")

    console_text.delete.assert_called_once_with(0, 'end')
    console_text.insert.assert_called_once_with(0, "Campo 'Telefone' só pode conter números.")
    
    assert verify is False