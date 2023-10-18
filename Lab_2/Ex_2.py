import numpy as np

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes(numbers):
    prime_numbers = [num for num in numbers if is_prime(num)]
    return prime_numbers


if __name__ == '__main__':

    find_primes(numbers)