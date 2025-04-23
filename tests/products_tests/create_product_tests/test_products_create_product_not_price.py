import pytest
from unittest.mock import MagicMock
from support.verify import Verify

def test_products_create_product_is_price():

    price_entry = MagicMock()
    price_entry.get.return_value = ""

    console_text = MagicMock()

    verify = Verify(console_text).verify_if_create_product_is_price("")

    console_text.delete.assert_called_once_with(0, 'end')
    console_text.insert.assert_called_once_with(0, "Campo 'Preço' não pode estar vazio.")
    
    assert verify is False