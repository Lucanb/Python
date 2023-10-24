def duplicateCount(list):
    unqEl = set()
    duplicateEl = set()
    
    for item in list:
        if list.count(item) > 1:
            unqEl.add(item)
        else:
            unqEl.add(item)
    
    return len(unqEl), len(unqEl)

if __name__ == '__main__':
    numberList = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
    result = duplicateCount(numberList)
    print(result) 
