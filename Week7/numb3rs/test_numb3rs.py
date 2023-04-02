from numb3rs import validate


def test_true():
    assert validate("0.0.0.0")
    assert validate("123.123.123.123")
    assert validate("255.255.255.255")


def test_false():
    assert not validate("0.0.0.0.")
    assert not validate("0.0.0")
    assert not validate("123.321.123.123")
    assert not validate("cat")
    assert not validate("123..123.123")
    assert not validate("1.1.1.1234")
