def verif_palindrom(number):
    number_string = str(number)
    return number_string == number_string[::-1]

if __name__ == '__main__':

    number = input("Enter a natural number' : ")
    if number.isdigit():
        number = int(number)

        if verif_palindrom(number):
            print(f"{number} is a palindrome")
        else:
            print(f"{number} is not a palindrome")
    else:
        print("Error: Please enter natural a number.")
