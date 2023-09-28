import pytest
import convertisseurs.complementadeux as cad


@pytest.mark.parametrize("value,expected", [("10001", 17), ("0", 0)])
def test_binary_to_decimal(value, expected):
    base_ten = cad.binary_to_decimal(value)
    assert base_ten == expected



