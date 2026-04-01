from src.kata.code import NUMBERS_UP_TO, fizz_buzz_whiz

# Code will return "Whiz" for primes <- COMPLETE
# Code will return "Fizz" for divisible with 3
# Code will return "Buzz" for divisible with 5 <- NEXT!
# Code will return "FizzBuzz" for divisible with 3 and 5 <- COMPLETE
# Code will return identity if there are no other rules
# Code will apply rules in correct restrictive order: -> prime -> 3&5 -> 5 -> 3 -> string of identity

# fmt: off
primes_up_to_100 = {
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
    31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
    73, 79, 83, 89, 97
} 
# fmt: on

numbers_divisible_by_three = {x for x in range(3, NUMBERS_UP_TO + 1, 3)}
numbers_divisible_by_five = {x for x in range(5, NUMBERS_UP_TO + 1, 5)}
numbers_divisible_by_three_and_five = (
    numbers_divisible_by_three & numbers_divisible_by_five
)


def test_primes():
    for number in primes_up_to_100:
        assert fizz_buzz_whiz(number) == "Whiz"


def test_three_and_five():
    for number in numbers_divisible_by_three_and_five:
        assert fizz_buzz_whiz(number) == "FizzBuzz"


def test_five():
    numbers = (
        numbers_divisible_by_five
        - numbers_divisible_by_three_and_five
        - primes_up_to_100
    )
    for number in numbers:
        assert fizz_buzz_whiz(number) == "Buzz"
