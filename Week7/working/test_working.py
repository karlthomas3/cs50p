import working
import pytest

def test_format():
    assert working.convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert working.convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert working.convert("8 PM to 8 AM") == "20:00 to 08:00"
    assert working.convert("8:00 PM to 8:00 AM") == "20:00 to 08:00"
    assert working.convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert working.convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"

def test_typo():
    with pytest.raises(ValueError):
        working.convert("8:60 AM to 4:60 PM")
        working.convert("9AM to 5PM")
        working.convert("09:00 to 17:00")
        working.convert("9 AM - 5 PM")
        working.convert("10:7 AM - 5:1 PM")
        working.convert("9 AM - 9 PM")
        working.convert("12:00 AM  12:00 PM")

def test_values():
    with pytest.raises(ValueError):
        working.convert("13 AM to 1 PM")
        working.convert("8 PM to 8:60 PM")

def test_no_to():
    with pytest.raises(ValueError):
        working.convert("9 AM 5 PM")