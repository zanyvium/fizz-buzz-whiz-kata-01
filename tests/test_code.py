from src.kata.code import NUMBERS_UP_TO, fizz_buzz_whiz

# Test will return identity for any number


def test_tmp_identity():
    for number in range(1, NUMBERS_UP_TO + 1):
        assert fizz_buzz_whiz(number) == number
