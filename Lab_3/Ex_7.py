from itertools import combinations

def setOperators(*args):
    finalDictionry = {}
    set = combinations(args, 2)
    
    for a, b in set:
        keyOp1 = f"{a} | {b}"
        keyOp2 = f"{a} & {b}"
        keyOp3 = f"{a} - {b}"
        keyOp4 = f"{b} - {a}"
        
        finalDictionry[keyOp1] = a | b
        finalDictionry[keyOp2] = a & b
        finalDictionry[keyOp3] = a - b
        finalDictionry[keyOp4] = b - a

    return finalDictionry
if __name__ == '__main__':

    setA = {1, 2}
    setB = {2, 3}

    finalDictionry = setOperators(setA, setB)
    for key, value in finalDictionry.items():
        print(f"{key}: {value}")