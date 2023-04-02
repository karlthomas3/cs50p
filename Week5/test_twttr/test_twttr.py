from twttr import shorten


def test_lower():
    assert shorten("aeiou") == ""


def test_upper():
    assert shorten("AEIOU") == ""

def test_hello():
    assert shorten("hello, world") == "hll, wrld"
    assert shorten("HELLO, WORLD") == "HLL, WRLD"

def test_num():
    assert shorten("1234567890") == "1234567890"