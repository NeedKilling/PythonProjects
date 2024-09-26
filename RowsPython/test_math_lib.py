import math_lib
test_res = []

def run_test(test_fanc):
    try:
        test_fanc()
        test_res.append(True)    
    except:     
        print(f"{test_fanc.__name__} faled")
        test_res.append(False)   

def test_int_add_float():
    # assert math_lib.int_add_float(5,3.2) == 5 + 3.2, "5 + 3.2 должно быть 8.2"
    # assert math_lib.int_add_float(-5,3.2) == -5 + 3.2, "-5 + 3.2 должно быть -1.8"
    # assert math_lib.int_add_float(5,-3.2) == 5 + (-3.2), "5 + (-3.2) должно быть 1.8"
    pass

def test_int_substruct_float():
    pass
    
def test_multiply_numbers():
    pass    

run_test(test_int_add_float)
run_test(test_int_substruct_float)

if sum(test_res) == 0:
    print("0%")
else:    
    print(f"{int(len(test_res)/sum(test_res))*100}%")
