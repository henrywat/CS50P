from fuel import convert, gauge
import pytest

def main():
    test_convert()
    test_gauge()

def test_convert():
    assert convert("1/4") == 25
    with pytest.raises(ZeroDivisionError):
        assert convert("1/0")
    with pytest.raises(ValueError):
        assert convert("3/2")

def test_gauge():
    assert gauge(33) == "33%"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"


if __name__ == "__main__":
    main()