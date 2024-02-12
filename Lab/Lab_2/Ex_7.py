
def verif_palindrome(n):
    return str(n) == str(n)[::-1]

def count_max_palindrome(list):
    count = 0
    max_palindrome = -1

    for element in list:
        if verif_palindrome(element):
            count += 1
            if max_palindrome == -1 or element > max_palindrome:
                max_palindrome = element

    return (count, max_palindrome)

if __name__ == '__main__':

    list = [12, 11411, 121, 235, 12344321, 6763]

    result = count_max_palindrome(list)
    print(result)