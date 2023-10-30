class Matrix:
    def __init__(self,n,m):
        self.rows = n
        self.columns = m
    
    def insert_element(value,i,j,self):
        if 0 <= i < self.rows and 0 <= j < self.columns:
            self.mat[i][j] = value
        else:
            raise IndexError("Out of range")

    def get_element(i,j,self):
        if 0 <= i < self.rows and 0 <= j < self.columns:
            return self.mat[i][j]
        else:
            raise IndexError("Out of range")
    
    def transpose(self):
        new_Mat = Matrix(self.columns, self.rows)
        for i in range(self.rows):
            for j in range(self.columns):
                new_Mat.set_element(j, i, self.data[i][j])
        return new_Mat
    
    def matrix_multiply(self, A):
        if self.columns != A.rows:
            raise ValueError("Dimension erorr")
        
        C = Matrix(self.rows, A.columns) 
        for i in range(self.rows):
            for j in range(A.columns):
                dot_product = sum(self.data[i][k] * A.data[k][j] for k in range(self.columns))
                C.set_element(i, j, dot_product)
        
        return C   

    def transformEL(self, lambdaFunct):
        for i in range(self.rows):
            for j in range(self.columns):
                self.set_element(i, j, lambdaFunct(self.get_element(i, j)))

if __name__ == '__main__':
    
    matrix = Matrix(3, 2)
    matrix.insert_element(0, 0, 6)
    matrix.insert_element(0, 1, 2)
    matrix.insert_element(1, 0, 4)
    matrix.insert_element(1, 1, 3)
    matrix.insert_element(2, 0, 5)
    matrix.insert_element(3, 2, 7)
    print(matrix)

    T = matrix.transpose()
    print(T)

    identity_matrix = Matrix(2, 3)
    identity_matrix.set_element(0, 0, 3)
    identity_matrix.set_element(0, 1, 0)
    identity_matrix.set_element(0, 2, 2)
    identity_matrix.set_element(1, 0, 1)
    identity_matrix.set_element(1, 1, 4)
    identity_matrix.set_element(1, 2, 7)

    result_matrix = matrix.matrix_multiply(identity_matrix)
    print(result_matrix)

    matrix.apply_transform(lambda x: x + x )
    print(matrix)

 











