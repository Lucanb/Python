import numpy as np

def sqt_operations(a, b):

    inter = list(set(a) & set(b))
    union = list(set(a) | set(b))
    A_diff = list(set(a) - set(b))
    B_diff = list(set(b) - set(a))
    return inter, union, A_diff, B_diff

if __name__ == '__main__':
    list_a = [12,4,2,5,7,12,3,45,2]
    list_b = [1,2,5,34,12,2,5,7,134,124]
    result = sqt_operations(list_a, list_b)
    
    print("Intersection:", result[0])
    print("Union:", result[1])
    print("A - B:", result[2])
    print("B - A:", result[3])