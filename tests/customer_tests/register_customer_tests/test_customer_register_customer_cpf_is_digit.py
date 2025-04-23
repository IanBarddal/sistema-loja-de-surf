import pytest
from unittest.mock import MagicMock
from support.verify import Verify

def test_customer_register_cpf_is_digit():

    cpf_entry = MagicMock()
    cpf_entry.get.return_value = "444.444.444-CC"

    console_text = MagicMock()

    verify = Verify(console_text).verify_if_cpf_is_digit("444.444.444-CC")

    console_text.delete.assert_called_once_with(0, 'end')
    console_text.insert.assert_called_once_with(0, "Campo 'CPF' só pode conter números, pontos e hífen.")
    
    assert verify is False