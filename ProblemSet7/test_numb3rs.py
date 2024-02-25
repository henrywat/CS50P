from numb3rs import validate
import pytest

def main():
    test_validate()


def test_validate():
    assert validate("1.2.3.4") == True
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.0") == True
    assert validate("255.255.255.255") == True
    assert validate("275.3.6.28") == False
    assert validate("cat") == False
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("127.300.1.2") == False
    assert validate("127.1.300.2") == False
    assert validate("127.1.2.300") == False
    assert validate("127.300.300.300") == False


if __name__ == "__main__":
    main()