import matrix_lib
test_res = []

def run_test(test_fanc):
    try:
        test_fanc()
        test_res.append(True)    
    except:     
        print(f"{test_fanc.__name__} faled")
        test_res.append(False)   

def test_get_matrix_size():
    assert matrix_lib.get_matrix_size([[1, 2, 3], [4, 5, 6]]) == (2, 3), "Размер матрицы должен быть (2, 3)"
    assert matrix_lib.get_matrix_size([[]]) == (1, 0), "Размер матрицы [ [] ] должен быть (1, 0)"
    assert matrix_lib.get_matrix_size([]) == (0, 0), "Размер пустой матрицы должен быть (0, 0)"

def test_NoolMatrix():
    assert matrix_lib.NoolMatrix(2, 3) == [[0, 0, 0], [0, 0, 0]], "Матрица 2x3 должна состоять из нулей"
    assert matrix_lib.NoolMatrix(3, 2) == [[0, 0], [0, 0], [0, 0]], "Матрица 3x2 должна состоять из нулей"

def test_TranspoceNoolMatrix():
    assert matrix_lib.TranspoceNoolMatrix(2, 3) == [[0, 0], [0, 0], [0, 0]], "Транспонированная матрица 2x3 должна быть 3x2"
    assert matrix_lib.TranspoceNoolMatrix(3, 2) == [[0, 0, 0], [0, 0, 0]], "Транспонированная матрица 3x2 должна быть 2x3"
def test_add_matrices():
    assert matrix_lib.add_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]]) == [[6, 8], [10, 12]], "Сложение матриц 2x2"
    assert matrix_lib.add_matrices([[1, 2], [3, 4]], [[1, 2, 3]]) == "error", "Ошибка при сложении матриц разной размерности"

def test_multiply_matrix_by_scalar():
    assert matrix_lib.multiply_matrix_by_scalar([[1, 2], [3, 4]], 2) == [[2, 4], [6, 8]], "Матрица 2x2, умноженная на 2"
    assert matrix_lib.multiply_matrix_by_scalar([[1, 2], [3, 4]], 0) == [[0, 0], [0, 0]], "Матрица 2x2, умноженная на 0"

def test_multiply_matrices():
    assert matrix_lib.multiply_matrices([[1, 2], [3, 4]],[[2, 0], [1, 2]]) == [[4, 4], [10, 8]], "Произведение матриц 2x2"
    assert matrix_lib.multiply_matrices([[1, 2], [3, 4]], [[1]]) == "error", "Ошибка при умножении матриц несовместимых размерностей"

def test_transpose_matrix():
    assert matrix_lib.transpose_matrix([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]], "Транспонирование матрицы 2x3"

def test_minor():
    assert matrix_lib.minor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, 1) == [[4, 6], [7, 9]], "Минор матрицы 3x3 с удалением 0-й строки и 1-го столбца"

def test_determinant():
    assert matrix_lib.determinant([[1, 2], [3, 4]]) == -2, "Определитель матрицы 2x2"

def test_lengthVector():
    assert matrix_lib.lengthVector([1, 2, 3]) == 3, "Длина вектора [1, 2, 3] должна быть 3"
    assert matrix_lib.lengthVector([]) == 0, "Длина пустого вектора должна быть 0"

def test_add_vectors():
    assert matrix_lib.add_vectors([1, 2, 3], [4, 5, 6]) == [5, 7, 9], "Сложение векторов [1, 2, 3] и [4, 5, 6]"
    assert matrix_lib.add_vectors([1, 2, 3], [1, 2]) == "error", "Ошибка при сложении векторов разной длины"

def test_multiply_vector_by_scalar():
    assert matrix_lib.multiply_vector_by_scalar([1, 2, 3], 2) == [2, 4, 6], "Умножение вектора [1, 2, 3] на 2"
    assert matrix_lib.multiply_vector_by_scalar([1, 2, 3], 0) == [0, 0, 0], "Умножение вектора [1, 2, 3] на 0"


run_test(test_multiply_vector_by_scalar)
run_test(test_add_vectors)
run_test(test_lengthVector)
run_test(test_determinant)
run_test(test_minor)
run_test(test_transpose_matrix)
run_test(test_multiply_matrices)
run_test(test_multiply_matrix_by_scalar)
run_test(test_add_matrices)
run_test(test_TranspoceNoolMatrix)
run_test(test_NoolMatrix)
run_test(test_get_matrix_size)

if sum(test_res) == 0:
    print("0%")
else:    
    print("Тест пройден на " f"{int(len(test_res)/sum(test_res))*100}%")
