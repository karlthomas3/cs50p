from um import count

def test_basic():
    assert count("um") == 1
    assert count("UM") == 1
    assert count(" um") == 1
    assert count("um ") == 1

def test_special():
    assert count("um.") == 1
    assert count("um,") == 1

def test_wrong():
    assert count("yum") == 0
    assert count("hum") == 0
    assert count("dumb") == 0

def test_sentence():
    assert count("Um, thanks for the album") == 1
    assert count("Um, thanks, um...") == 2
