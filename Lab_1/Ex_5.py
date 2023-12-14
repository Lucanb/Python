def spiral_write(mat):
    res = []
    while mat:
        res += mat[0]
        mat = list(zip(*mat[1:]))[::-1]
    return ''.join(res)

if __name__ == '__main__':
 matrix = [
    ['f', 'i', 'r', 's'],
    ['n', '_', 'l', 't'],
    ['o', 'b', 'a', '_'],
    ['h', 't', 'y', 'p']
 ]
 print(spiral_write(matrix))