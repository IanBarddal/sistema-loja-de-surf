import pytest
from unittest.mock import MagicMock
from support.verify import Verify

def test_products_create_product_price_is_digit():

    price_entry = MagicMock()
    price_entry.get.return_value = "230A"

    console_text = MagicMock()

    verify = Verify(console_text).verify_if_create_product_price_is_digit("230A")

    console_text.delete.assert_called_once_with(0, 'end')
    console_text.insert.assert_called_once_with(0, "Campo 'Preço' só pode conter números.")
    
    assert verify is False