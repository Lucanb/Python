import numpy as np

def fib_gen(n):
    fib_seq = []
    
    if n <= 0:
        return fib_seq
    elif n == 1:
        fib_seq.append(0)
    elif n >= 2:
        fib_seq.extend([0, 1])
    
    while len(fib_seq) < n:
        num = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(num)
    
    return fib_seq

if __name__ == '__main__':
    n = input("'Enter a natural number : '")
    if n.isdigit():
        n = int(n)
        fib_numbers = fib_gen(n)
        if fib_numbers:
         print(fib_numbers)
        else:
         print('Enter a number > 0')
    else :
        print('Error , you entered a string or a negative number')