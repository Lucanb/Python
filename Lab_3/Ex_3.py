def Compare_Dictionaries(dict_a, dict_b):
    if type(dict_a) != type(dict_b):
        return False

    if isinstance(dict_a, dict):
        if set(dict_a.keys()) != set(dict_b.keys()):
            return False

        for key in dict_a:
            if not Compare_Dictionaries(dict_a[key], dict_b[key]):
                return False

    elif isinstance(dict_a, (list, tuple, set)):
        if len(dict_a) != len(dict_b):
            return False

        for item_a, item_b in zip(dict_a, dict_b):
            if not Compare_Dictionaries(item_a, item_b):
                return False

    else:
        if dict_a != dict_b:
            return False

    return True

if __name__ == '__main__':
  dict1 = {"a": 1, "b": [2, 3, {"c": 4}], "d": {"e": 5}}
  dict2 = {"a": 1, "b": [2, 3, {"c": 4}], "d": {"e": 5}}
  dict3 = {"a": 1, "b": [2, 3, {"c": 4}], "d": {"e": 7}}

  result1 = Compare_Dictionaries(dict1, dict2)
  result2 = Compare_Dictionaries(dict1, dict3)
  print(result1)
  print(result2)


# dict1 = {"a": 1, "b": [2, 3, {"c": 4}], "d": {"e": 5}}
# dict2 = {"a": 1, "b": [2, 3, {"c": 4}], "d": {"e": 5}}
 
# result1 = all((dict1.get(k) == v for k, v in dict2.items()))
# print(result1)