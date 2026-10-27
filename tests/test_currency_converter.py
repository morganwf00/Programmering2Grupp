from functions.currency_converter import convert_to_sek


# Test att konvertering fungerar bra
def test_convert_to_sek():
    svar = convert_to_sek(100, 11.14)
    assert svar == 1114.0
