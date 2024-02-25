import pytest
from seasons import convert_to_minutes

def test_seasons():
    assert convert_to_minutes(1999, 1, 1) == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert_to_minutes(1999, 12, 31) == "One thousand, four hundred forty minutes"
    assert convert_to_minutes(1970, 1, 1) == "Fifteen million, seven hundred seventy-eight thousand eighty minutes"
    assert convert_to_minutes(2001, 1, 1) == "One million, fifty-one thousand, two hundred minutes"
    assert convert_to_minutes(1995, 1, 1) == "Two million, six hundred twenty-nine thousand, four hundred forty minutes"
    assert convert_to_minutes(2020, 6, 1) == "Six million, ninety-two thousand, six hundred forty minutes"
    assert convert_to_minutes(1998, 6, 20) == "Eight hundred six thousand, four hundred minutes"
    #assert convert_to_minutes(29, 1, 2983) == "Invalid Date"
    with pytest.raises(ValueError):
        convert_to_minutes(29, 1, 2983)
    #with pytest.raises(ValueError) as excinfo:
    #    convert_to_minutes(29, 1, 2983)
    #assert str(excinfo.value) == "Invalid Date"