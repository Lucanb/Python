def count_bits(number):
    count = 0
    while number > 0:
        count += number & 1
        number = number>>1

    return count

if __name__ == '__main__':

    number = input("Enter a natural number' : ")
    if number.isdigit():
        number = int(number)
        print(count_bits(number))
    else:
        print("Error: Please enter natural a number.")