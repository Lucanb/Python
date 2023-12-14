def get_the_number(text):
    number = ""
    sw = False

    for char in text:
        if char.isdigit():
            number += char
            sw = True
        elif sw:
            break

    if sw:
        return int(number)
    else:
        return -1

if __name__ == '__main__':
    text = input("'Please enter a text : '")
    print(get_the_number(text))