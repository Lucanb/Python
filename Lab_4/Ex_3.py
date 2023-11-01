class Matrix:
    def __init__(self, n, m):
        self.rows = n
        self.columns = m
        self.mat = [[0] * m for _ in range(n)]

    def insert_element(self, value, i, j):
        if 0 <= i < self.rows and 0 <= j < self.columns:
            self.mat[i][j] = value
        else:
            raise IndexError("Out of range")

    def get_element(self, i, j):
        if 0 <= i < self.rows and 0 <= j < self.columns:
            return self.mat[i][j]
        else:
            raise IndexError("Out of range")

    def transpose(self):
        new_Mat = Matrix(self.columns, self.rows)
        for i in range(self.rows):
            for j in range(self.columns):
                new_Mat.insert_element(self.mat[i][j], j, i)
        return new_Mat

    def matrix_multiply(self, A):
        if self.columns != A.rows:
            raise ValueError("Dimension error")

        C = Matrix(self.rows, A.columns)
        for i in range(self.rows):
            for j in range(A.columns):
                dot_product = sum(self.mat[i][k] * A.get_element(k, j) for k in range(self.columns))
                C.insert_element(dot_product, i, j)

        return C

    def transformEL(self, lambdaFunct):
        for i in range(self.rows):
            for j in range(self.columns):
                self.insert_element(lambdaFunct(self.get_element(i, j)), i, j)

    def __str__(self):
        result = ""
        for i in range(self.rows):
            result += "    ".join(map(str, self.mat[i])) + "\n" + "\n"
        return result


matrix = Matrix(3, 2)
print("Initial Matrix:")
print(matrix)

matrix.insert_element(6, 0, 0)
matrix.insert_element(2, 0, 1)
matrix.insert_element(4, 1, 0)
matrix.insert_element(3, 1, 1)
matrix.insert_element(5, 2, 0)
matrix.insert_element(7, 2, 1)
print("Matrix After Insertion:")
print(matrix)

T = matrix.transpose()
print("Transpose of the Matrix:")
print(T)

identity_matrix = Matrix(2, 3)
identity_matrix.insert_element(3, 0, 0)
identity_matrix.insert_element(0, 0, 1)
identity_matrix.insert_element(2, 0, 2)
identity_matrix.insert_element(0, 1, 0)
identity_matrix.insert_element(4, 1, 1)
identity_matrix.insert_element(7, 1, 2)

result_matrix = matrix.matrix_multiply(identity_matrix)
print("Matrix After Multiplication:")
print(result_matrix)

matrix.transformEL(lambda x: x + x)
print("Matrix After Transformation:")
print(matrix)