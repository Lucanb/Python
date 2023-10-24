
def Compare_Dictionaries(dict_a,dict_b):

    if(set(dict_a)!=set(dict_b)):
      return False
    
    for key in dict_a:
       type_a = type(dict_a[key])
       type_b = type(dict_b[key])

       if type_a in (int, float, str, bool):
            if dict_a[key] != dict_b[key]:
                return False
            elif type_a in (list, tuple, set):
             if len(dict_a[key]) != len(dict_b[key]):
                return False
             for i in range(len(dict_a[key])):
                if not Compare_Dictionaries(dict_a[key][i], dict_b[key][i]):
                    return False
            elif type_a == dict:
                 if not Compare_Dictionaries(dict_a[key], dict_b[key]):
                    return False

    return True




if __name__ == '__main__':
  dict1 = {"a": 1, "b": [2, 3, {"c": 4}], "d": {"e": 5}}
  dict2 = {"a": 1, "b": [2, 3, {"c": 4}], "d": {"e": 5}}
  dict3 = {"a": 1, "b": [2, 3, {"c": 4}], "d": {"e": 6}}

result1 = Compare_Dictionaries(dict1, dict2)
result2 = Compare_Dictionaries(dict1, dict3)

print(result1)
print(result2)