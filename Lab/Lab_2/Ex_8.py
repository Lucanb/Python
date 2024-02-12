
def div_char(x=1, list=[], flag=True):
    results = []
    for string in list:
        chars = []
        for char in string:
            code_ascii = ord(char)
            if (code_ascii % x == 0 and flag) or (code_ascii % x != 0 and not flag):
                chars.append(char)
        results.append(chars)
    
    return results


if __name__ == '__main__':

    x = 2
    list = ["test", "hello", "lab002"]
    flag = False

    result = div_char(x, list, flag)
    print(result)