NUMBERS_UP_TO = 100


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def fizz_buzz_whiz(number: int) -> str:
    number_div_by_5 = number % 5 == 0
    number_div_by_3 = number % 3 == 0
    if is_prime(number):
        return "Whiz"
    elif number_div_by_3 and number_div_by_5:
        return "FizzBuzz"
    elif number_div_by_5:
        return "Buzz"
    elif number_div_by_3:
        return "Fizz"
