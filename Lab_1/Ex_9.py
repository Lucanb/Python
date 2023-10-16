def max_letters(text):
    text = text.lower()
    letter_vec = {}

    for letter in text:
        if letter.isalpha():
            if letter in letter_vec:
                letter_vec[letter] += 1
            else:
                letter_vec[letter] = 1

    max_letter = max(letter_vec, key=letter_vec.get)

    return max_letter, letter_vec[max_letter]

if __name__ == '__main__':
    text = input("'Please enter a text : ' ")  # Replace with your input string
    max_letter, count = max_letters(text)
    print(f"The most common letter is '{max_letter}' with a count of {count}.")
