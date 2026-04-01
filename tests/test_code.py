from src.kata.code import fizz_buzz_whiz

# Test will return identity for any number
# fmt: off
primes_up_to_100 = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
    31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
    73, 79, 83, 89, 97
] 
# fmt: on


def test_tmp_identity():
    for number in primes_up_to_100:
        assert fizz_buzz_whiz(number) == str(number)
