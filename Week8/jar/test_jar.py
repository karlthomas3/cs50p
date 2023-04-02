from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError):
        jar = Jar(-2)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert jar.deposit(6) == 6
    with pytest.raises(ValueError):
        jar.deposit(7)


def test_withdraw():
    jar = Jar()
    jar.deposit(3)
    assert jar.withdraw(2) == 1
    with pytest.raises(ValueError):
        jar.withdraw(4)