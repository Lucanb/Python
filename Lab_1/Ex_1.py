import numpy as np

def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_multiple_cmmdc():
    elements = []
    while True:
        num_input = input("Enter numbers or 'exit to quit'")
        if num_input == 'exit':
            break
        if num_input.isdigit():
            number = int(num_input)
            if number > 0:
                elements.append(number)
            else:
                print("Error: Please enter natural number.")
        else:
            print("Error: Please enter natural number.")
    if elements:
       prev = elements[0]
       gcd = prev
       for element in elements[1:]:
        gcd = calculate_gcd(element,prev)
        if gcd == 1:
            print(gcd)
            return
        prev = gcd
       print(gcd)
    else:
        print("you didn't enter the numbers!")

if __name__ == '__main__':
    calculate_multiple_cmmdc()
