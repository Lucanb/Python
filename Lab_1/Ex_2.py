import  numpy as np
def calculate_vowels():
 num_input = input("Enter a string or 'exit to quit'")
 if num_input.isdigit():
     print("no leters inserted")
 else:
     number = 0
     for letter in num_input:
       if(letter.lower() == 'a' or letter.lower() == 'e' or letter.lower() == 'i' or letter.lower() == 'o' or letter.lower() == 'u'):
               number =  number + 1
     print(number)

if __name__ == '__main__':
    calculate_vowels()