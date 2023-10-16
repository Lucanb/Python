def cont_words(text):
    words = text.split()
    return len(words)

if __name__ == '__main__':
    text = input("'Please enter a text : ' ")
    print(f"Number of words is : '{cont_words(text)}'")