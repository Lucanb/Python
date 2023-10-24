
def Create_dictionr_Word(string):

    dict = {}
    for letter in string:
        if letter.isalnum():
            letter = letter.lower()

            if letter in dict:
                dict[letter] = dict[letter] + 1
            else:
                dict[letter] = 1
    return dict


if __name__ == '__main__':
    input_string = "Ana has apples."
    result = Create_dictionr_Word(input_string)
    print(result)

