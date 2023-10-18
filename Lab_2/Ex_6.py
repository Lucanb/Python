from collections import Counter

def count_item(element, *lists):
    lists = [item for sublist in lists for item in sublist]
    vec_counter = Counter(lists)
    result = [item for item, count in vec_counter.items() if count == element]
    return result

if __name__ == '__main__':

    list1 = [1, 2, 3]
    list2 = [2, 3, 4]
    list3 = [4, 5, 6]
    list4 = [4, 1, "test"]
    count = 2

    res = count_item(count, list1, list2, list3, list4)
    print(res)