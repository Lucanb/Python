import numpy as np

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def list_primes(numbers):
    primes = [i for i in numbers if is_prime(i)]
    return primes

if __name__ == '__main__':
    n = int(input("Enter number of elements : "))

    numbers =list(map(int, 
    input("\nEnter the numbers : ").strip().split()))[:n]
    prime_numbers = list_primes(numbers)
    print(prime_numbers)