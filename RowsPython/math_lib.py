def get_matrix_size(matrix: list) -> tuple:
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    return rows,cols

def add_matrices(matrix_a: list, matrix_b: list) -> list :
    noolMatrix = list(matrix_a)
    
    if get_matrix_size(matrix_a) != get_matrix_size(matrix_b):
        
        return 'error'
    else:
        for i in range(len(matrix_a)):
            for j in range(len(matrix_a[0])):
                print(matrix_a[i][j],"  +  ",matrix_b[i][j])
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
    print(matrixOne)
    print(matrixTwo)
    if(matrixOne[1] != matrixTwo[0]):
        return "error"
    else:
        return "norm"
        # for i in matrixOne:
        #     return matrixOne[i]*matrixTwo[i]

print(multiply_matrices([[1,2],[3,4]],[[5,6],[7,8]]))
#print(multiply_matrix_by_scalar([[1,2],[3,4]],2))   
#print(add_matrices([[1,2],[3,4]],[[5,6],[7,8]]))
#print(get_matrix_size([[1,2],[1,2]]))
