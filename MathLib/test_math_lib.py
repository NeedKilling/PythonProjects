import math_lib
import math

test_res = []

def run_test(test_fanc):
    try:
        test_fanc()
        test_res.append(True)    
    except:     
        print(f"{test_fanc.__name__} faled")
        test_res.append(False)   

def test_int_add_float():
    assert math_lib.int_add_float(5,3.2) == 5 + 3.2, "5 + 3.2 должно быть 8.2"
    assert math_lib.int_add_float(-5,3.2) == -5 + 3.2, "-5 + 3.2 должно быть -1.8"
    assert math_lib.int_add_float(5,-3.2) == 5 + (-3.2), "5 + (-3.2) должно быть 1.8"

def test_int_substruct_float():
    assert math_lib.int_substract_float(5, 3.2) == 5 - 3.2, "5 - 3.2 must be 1.8"
    assert math_lib.int_substract_float(-5, 3.2) == -5 - 3.2, "-5 - 3.2 must be -8.2"
    assert math_lib.int_substract_float(5, -3.2) == 5 - (-3.2), "5 - (-3.2) must be 8.2"
    
def test_multiply_numbers():
    assert math_lib.multiply_numbers(5, 1.5) == 5 * 1.5, "5 * 1.5 must be 7.5"
    assert math_lib.multiply_numbers(5, 0.0) == 5 * 0.0, "5 *  0 must be 0"
    assert math_lib.multiply_numbers(-5, -1.5) == -5 * -1.5, "-5 * -1.5 must be 7.5"
    
def test_devide_numbers():
    assert math_lib.devide_numbers(5.5, 0.5) == 5.5 / 0.5, "5.5 / 0.5 must be 11.0"
    assert math_lib.devide_numbers(-5.5, 0.5) == -5.5 / 0.5, "-5.5 / 0.5 must be -11.0"
    
def test_is_even():
    assert math_lib.is_even(2) == True, "2 must be true"
    assert math_lib.is_even(3) == False, "3 must be false"
    
def test_factorial():
    assert math_lib.factorial(4) == math.factorial(4), "facctorial(4) must be 24"
    
def test_sin_approximation():
    epsilon = 0.00001
    assert math_lib.sin_approximation(30*math.pi/180, epsilon) - math.sin(30*math.pi/180) < epsilon, "sin(30)"
    assert math_lib.sin_approximation(0*math.pi/180, epsilon) - math.sin(0*math.pi/180) < epsilon, "sin(0)"     
    
def test_cos_approximation():
    epsilon = 0.00001
    assert (math_lib.cos_approximation(30*math.pi/180, epsilon) - math.cos(30*math.pi/180) < epsilon), "cos(30)"
    assert (math_lib.cos_approximation(0*math.pi/180, epsilon) - math.cos(0*math.pi/180) < epsilon), "cos(0)"
    
def test_custom_ceil():
    assert math_lib.custom_ceil(3.5) == math.ceil(3.5), "3.5 must be 4"
    assert math_lib.custom_ceil(-3.5) == math.ceil(-3.5), "-3.5 must be -3"
    
def test_custom_floor():
    assert math_lib.custom_floor(3.5) == math.floor(3.5), "3.5 must be 3"
    assert math_lib.custom_floor(-3.5) == math.floor(-3.5), "-3.5 must  be  -4"
    
run_test(test_int_add_float)
run_test(test_int_substruct_float)
run_test(test_multiply_numbers)
run_test(test_devide_numbers)
run_test(test_is_even)
run_test(test_factorial)
run_test(test_sin_approximation)
run_test(test_cos_approximation)
run_test(test_custom_ceil)
run_test(test_custom_floor)

if sum(test_res) == 0:
    print("0%")
else:    
    print("Тест пройден на " f"{int(len(test_res)/sum(test_res))*100}%")

