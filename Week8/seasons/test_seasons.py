from seasons import dob_get, time_diff
import pytest

def test_format():
    with pytest.raises(ValueError):
        dob_get("cat")
        dob_get("1234/12/12")
        dob_get("1999-02-30")
        dob_get("july 31, 1984")