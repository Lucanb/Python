import  numpy as np

def new_case(str):
    return ''.join(['_' + i.lower() if i.isupper()
                    else i for i in str]).lstrip('_')

if __name__ == '__main__':
    print(new_case("AmMersLaMare"))