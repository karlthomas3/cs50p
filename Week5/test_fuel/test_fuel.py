from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("1/1") == 100
    assert convert("1/2") == 50
    assert convert("1/100") == 1


def test_convertv():
    with pytest.raises(ValueError):
        convert("2/1")
        convert("a/1")
        convert("1/a")


def test_convertz():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
