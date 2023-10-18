import numpy as np

def put_zero(mat):
    if not mat:
        return mat
    rows = len(mat)
    cols = len(mat[0])
    for i in range(rows):
        for j in range(cols):
            if i > j:
                mat[i][j] = 0
    return mat

if __name__ == '__main__':
    mat = [
    [12, 3, 7],
    [1, 4, 5],
    [2, 17, 9]
]

result = put_zero(mat)
for row in result:
    print(row)