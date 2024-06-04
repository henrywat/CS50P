import bank

def main():
    test_greeting()

def test_greeting():
    assert bank.value("hello") == 0
    assert bank.value("HELLO") == 0
    assert bank.value("hi") == 20
    assert bank.value("HI") == 20
    assert bank.value("thanks") == 100
    assert bank.value("THANKS") == 100
    assert bank.value("--thanks") == 100
    assert bank.value("P@ssw0rd") == 100


if __name__ == "__main__":
    main()

