from main import luhn

def test_luhn_valid():
    assert luhn("4532015112830366") == True

def test_luhn_invalid():
    assert luhn("123456789") == False
    