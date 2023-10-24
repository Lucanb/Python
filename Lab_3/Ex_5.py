def verifDictionary(rules, dict):
    for key, prefix, middle, suffix in rules:
        if key in dict:
            value = dict[key]
            if not value.startswith(prefix):
                return False
            if middle not in value[1:-1]:
                return False
            if not value.endswith(suffix):
                return False
        else:
            return False

    return True

if __name__ == '__main__':

    
    validation_rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
    data = {
        "key1": "come inside, it's too cold out",
        "key2": "start with winter and middle text",
        "key3": "this is not valid"
    }

    result = verifDictionary(validation_rules, data)
    print(result)