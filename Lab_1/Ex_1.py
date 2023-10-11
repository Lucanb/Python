# This is a sample Python script.
import numpy as np


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
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



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calculate_multiple_cmmdc()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
