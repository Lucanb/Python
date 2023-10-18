def list_ryme(elements):
    RetR = {}
    for element in elements:
        piece = element[-2:]
        if piece not in RetR:
            RetR[piece] = []
        RetR[piece].append(element)
    list_Ret = RetR.values()
    return list_Ret

if __name__ == '__main__':
    
    list = ['ana', 'banana', 'carte', 'arme', 'parte']
    result = list_ryme(list)
    print(result)