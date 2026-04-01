from src.kata.code import fizz_buzz_whiz

# Code will return "Whiz" for primes
# Code will return "Fizz" for divisible with 3
# Code will return "Buzz" for divisible with 5
# Code will return "FizzBuzz" for divisible with 3 and 5
# Code will return identity if there are no other rules
# Code will apply rules in correct restrictive order: -> prime -> 3&5 -> 5 -> 3 -> string of identity

# fmt: off
primes_up_to_100 = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
    31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
    73, 79, 83, 89, 97
] 
# fmt: on


def test_primes():
    for number in primes_up_to_100:
        assert fizz_buzz_whiz(number) == "Whiz"
