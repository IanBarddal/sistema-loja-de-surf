import pytest
from unittest.mock import MagicMock
from support.verify import Verify

def test_customer_edit_not_cpf():

    id_entry = MagicMock()
    id_entry.get.return_value = ""

    console_text = MagicMock()

    verify = Verify(console_text).verify_if_edit_is_id("")

    console_text.delete.assert_called_once_with(0, 'end')
    console_text.insert.assert_called_once_with(0, "Campo 'ID do Cliente' não pode estar vazio.")
    
    assert verify is False