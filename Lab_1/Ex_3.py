import  numpy as np
def calculate_occurences():
    string_1 = input('The first string : ')
    string_2 = input('The second string : ')
    print('string1 appears into second string  :', string_2.count(string_1))

if __name__ == '__main__':
    calculate_occurences()