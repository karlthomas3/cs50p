from bank import value

def test_h():
    assert value("hola") == 20
    assert value("hel") == 20
    assert value("help") == 20

def test_hello():
    assert value("hello there!") == 0
    assert value("hello and go away") == 0
    
def test_nope():
    assert value("I fart in your general direction!") == 100
    assert value("Your mother was a hamster and your father smelled of elderberries") == 100

def test_case():
    assert value("HeLLo") == 0
    assert value("hOla") == 20
    assert value("Go AwAy") == 100
