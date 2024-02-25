import twttr

def main():
    test_twttr()

def test_twttr():
    assert twttr.shorten("twitter") == "twttr"
    assert twttr.shorten("HELLO") == "HLL"
    assert twttr.shorten("123") == "123"
    assert twttr.shorten(",./") == ",./"
    assert twttr.shorten("P@ssw0rd") == "P@ssw0rd"

if __name__ == "__main__":
    main()