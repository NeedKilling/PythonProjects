def get_matrix_size(matrix: list) -> tuple:
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    return rows,cols


def NoolMatrix(rows_matrix_a: int, cols_matrix_b: int)-> list:
    matrix = list()
    for i in range(rows_matrix_a):
        row = list()
        for j in range(cols_matrix_b):
            row.append(0)
        matrix.append(row)
    # for row in matrix:
    #     print(row)
    return matrix
def TranspoceNoolMatrix(rows_matrix_a: int, cols_matrix_b: int)-> list:
    matrix = list()
    for i in range(cols_matrix_b):
        row = list()
        for j in range(rows_matrix_a):
            row.append(0)
        matrix.append(row)
    # for row in matrix:
    #     print(row)
    return matrix


def add_matrices(matrix_a: list, matrix_b: list) -> list :
    matrixOne = get_matrix_size(matrix_a)
    matrixTwo = get_matrix_size(matrix_b)
    noolMatrix = NoolMatrix(matrixOne[0],matrixTwo[1])
    
    if matrixOne != matrixTwo:
        return 'error'
    else:
        for i in range(matrixOne[0]):
            for j in range(matrixTwo[1]):
                # print(matrix_a[i][j],"  +  ",matrix_b[i][j])
                noolMatrix[i][j] = matrix_a[i][j] + matrix_b[i][j] 
        return noolMatrix
         
def multiply_matrix_by_scalar(matrix: list, scalar: float) -> list:
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] *= scalar
    return matrix            
                
def multiply_matrices(matrix_a: list, matrix_b: list) -> list:
    
    matrixOne = get_matrix_size(matrix_a)
    matrixTwo = get_matrix_size(matrix_b)
    noolMatrix = NoolMatrix(matrixOne[0],matrixTwo[1])
   
    if(matrixOne[1] == matrixTwo[0] and matrixOne[0] == matrixTwo[1]):

        for i in range(matrixOne[0]):
            for j in range(matrixTwo[1]):
                for k in range(matrixOne[1]):
                    # print(matrix_a[i][k],"  ",matrix_b[k][j])
                    noolMatrix[i][j] += matrix_a[i][k] * matrix_b[k][j]
                       
        return noolMatrix
    else:
        return "error"
        
def transpose_matrix(matrix: list) -> list:
    
    matrixSize = get_matrix_size(matrix)
    noolMatrix = TranspoceNoolMatrix(matrixSize[0],matrixSize[1])

    for i in range(matrixSize[0]):
        for j in range(matrixSize[1]):
            noolMatrix[j][i] = matrix[i][j]
    return noolMatrix

def minor(matrix: list, row: int, col: int) -> list:
   
    return [i[:col] + i[col+1:] for i in (matrix[:row] + matrix[row+1:])]

def determinant(matrix: list) -> float:
   
    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for i in range(len(matrix)):
        minor = minor(matrix, 0, i)  
        det += ((-1) ** i) * matrix[0][i] * determinant(minor)  

    return det

def lengthVector(vector: list) -> int:
    counter = 0
    for i in vector:
        counter += 1
    return counter

def add_vectors(vector_a: list, vector_b: list) -> list:
    noolVector = list()
    if lengthVector(vector_a) != lengthVector(vector_b):
        return "error"
    else:
        for i in range(lengthVector(vector_a)):
            noolVector.append((vector_a[i] + vector_b[i]))
        return noolVector

def multiply_vector_by_scalar(vector: list, scalar: float) -> list:
    noolVector = list()
    for i in range(lengthVector(vector)):
        noolVector.append(vector[i]*scalar)
    return noolVector


# print(multiply_vector_by_scalar([1,2],2))
# print(add_vectors([1,2],[3,4]))
# print(lengthVector([1,2]))
#print(determinant([[1,2],[3,4]]))
# print(transpose_matrix([[1,2,3],[3,4,3],[5,6,3]]),"tran")
# print(multiply_matrices([[1,2,3],[3,4,3]],[[5,6],[7,8],[3,4]]),"multi")
# print(multiply_matrix_by_scalar([[1,2],[3,4]],2),"scalar")   
# print(add_matrices([[1,2],[3,4]],[[5,6],[7,8]]),"add")
# print(get_matrix_size([[1,2],[1,2]]),"size")

