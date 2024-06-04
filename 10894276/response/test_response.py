import pytest
from response import validate

def test_validate():
    assert validate("malan") == "Invalid"
    assert validate("malan at harvard dot edu") == "Invalid"
    assert validate("malan@harvard.edu") == "Valid"
    assert validate("henrywat@gmail.com") == "Valid"
    assert validate("malan@@@harvard.edu") == "Invalid"
    assert validate("malan@cs.harvard.edu") == "Valid"
    assert validate("malan@cs..harvard.edu") == "Invalid"
