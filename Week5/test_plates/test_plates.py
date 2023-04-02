import plates


def test_two_letters():
    assert plates.is_valid("CS50") == True
    assert plates.is_valid("C550") == False


def test_char_count():
    assert plates.is_valid("cs5000") == True
    assert plates.is_valid("cs50000") == False


def test_num_check():
    assert plates.is_valid("aaa222") == True
    assert plates.is_valid("aaa22a") == False
    assert plates.is_valid("cs50") == True
    assert plates.is_valid("cs05") == False


def test_char_check():
    assert plates.is_valid("cs50 ") == False
    assert plates.is_valid("cs50.") == False
    assert plates.is_valid("cs50,") == False
    assert plates.is_valid("cs50!") == False
