def go_mapping(dictionary):
    viz = set()
    result = []

    key = "start"
    while key not in viz:
        viz.add(key)
        result.append(dictionary[key])
        key = dictionary[key]

    return result
if __name__ == '__main__':

    dictionary = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
    result = go_mapping(dictionary)
    print(result)
