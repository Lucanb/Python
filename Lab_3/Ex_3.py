
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
            elif type_a is dict:
                 if not Compare_Dictionaries(dict_a[key], dict_b[key]):
                    return False

    return True




if __name__ == '__main__':
  dict1 = {"a": 1, "b": [2, 3, {"c": 4}], "d": {"e": 5}}
  dict2 = {"a": 1, "b": [2, 3, {"c": 4}], "d": {"e": 5}}

result1 = Compare_Dictionaries(dict1, dict2)

print(result1)




# dict1 = {"a": 1, "b": [2, 3, {"c": 4}], "d": {"e": 5}}
# dict2 = {"a": 1, "b": [2, 3, {"c": 4}], "d": {"e": 5}}
 
# result1 = all((dict1.get(k) == v for k, v in dict2.items()))
# print(result1)