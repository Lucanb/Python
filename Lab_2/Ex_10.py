def shuffle_list(*lists):
    maximum = max(len(index) for index in lists)
    res = []

    for i in range(maximum):
        elements = [index[i] if i < len(index) else None for index in lists]
        res.append(tuple(elements))

    return res

if __name__ == '__main__':

    list1 = [1, 2, 3]
    list2 = [5, 6, 7]
    list3 = ["a", "b", "c"]

    res = shuffle_list(list1, list2, list3)
    print(res)