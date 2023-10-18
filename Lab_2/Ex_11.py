def sort_key(key):
        if len(key) > 1 and len(key[1]) >= 3:
            return key[1][2]
        else:
            return ''
        
def sort_3d_list(list):
    sort_list = sorted(list, key=sort_key)
    return sort_list

if __name__ == '__main__':
    list = [('abc', 'bcd'), ('abc', 'zza')]
    res = sort_3d_list(list)
    print(res)