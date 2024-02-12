def verigArgs(*args, **kwargs):
    
    valueSet = set(kwargs.values())
    count = 0
    for arg in args:
        if arg in valueSet:
            count += 1
    return count

if __name__ == '__main__':
    result = verigArgs(1, 2, 3, 4, x=1, y=2, z=3, w=5)
    print(result)
