def pers_obs(mat):
    seats = []

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            height = mat[i][j]
            verif = False

            for k in range(i):
                if mat[k][j] >= height:
                    verif = True
                    break

            if verif:
                seats.append((i, j))

    return seats

if __name__ == '__main__':

    stadium = [
        [1, 2, 3, 2, 1, 1],
        [2, 4, 4, 3, 7, 2],
        [5, 5, 2, 5, 6, 4],
        [6, 6, 7, 6, 7, 5]
    ]

    persons = pers_obs(stadium)
    print(persons)