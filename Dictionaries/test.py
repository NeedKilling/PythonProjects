import dictionariesSets

test_res = []

def run_test(test_fanc):
    try:
        test_fanc()
        test_res.append(True)    
    except:     
        print(f"{test_fanc.__name__} faled")
        test_res.append(False)   

periodic_table = {
    1: {"name": "Hydrogen", "symbol": "H", "atomic_mass": 1.008},
    2: {"name": "Helium", "symbol": "He", "atomic_mass": 4.0026},
    3: {"name": "Lithium", "symbol": "Li", "atomic_mass": 6.94},
    4: {"name": "Beryllium", "symbol": "Be", "atomic_mass": 9.0122},
    5: {"name": "Boron", "symbol": "B", "atomic_mass": 10.81},
    6: {"name": "Carbon", "symbol": "C", "atomic_mass": 12.011},
    7: {"name": "Nitrogen", "symbol": "N", "atomic_mass": 14.007},
    8: {"name": "Oxygen", "symbol": "O", "atomic_mass": 15.999},
    9: {"name": "Fluorine", "symbol": "F", "atomic_mass": 18.998},
    10: {"name": "Neon", "symbol": "Ne", "atomic_mass": 20.180},
    11: {"name": "Sodium", "symbol": "Na", "atomic_mass": 22.990},
    12: {"name": "Magnesium", "symbol": "Mg", "atomic_mass": 24.305},
    13: {"name": "Aluminium", "symbol": "Al", "atomic_mass": 26.982},
    14: {"name": "Silicon", "symbol": "Si", "atomic_mass": 28.085},
    15: {"name": "Phosphorus", "symbol": "P", "atomic_mass": 30.974},
    16: {"name": "Sulfur", "symbol": "S", "atomic_mass": 32.06},
    17: {"name": "Chlorine", "symbol": "Cl", "atomic_mass": 35.45},
    18: {"name": "Argon", "symbol": "Ar", "atomic_mass": 39.948},
    19: {"name": "Potassium", "symbol": "K", "atomic_mass": 39.098},
    20: {"name": "Calcium", "symbol": "Ca", "atomic_mass": 40.078}
}

def test_create_dict():
    assert dictionariesSets.create_dict([1, 2, 3, 4], ["a", "b", "c", "d"]) == {1: "a", 2: "b", 3: "c", 4: "d"}, "Ошибка при создании словаря"
    assert dictionariesSets.create_dict([1, 2], ["a", "b", "c"]) == {}, "Списки разной длины должны возвращать пустой словарь"
    assert dictionariesSets.create_dict([], []) == {}, "Пустые списки должны возвращать пустой словарь"

def test_get_value():
    assert dictionariesSets.get_value(periodic_table, 1) == {"name": "Hydrogen", "symbol": "H", "atomic_mass": 1.008}, "верное значение для ключа 1"
    assert dictionariesSets.get_value(periodic_table, 21) is None, "Для несуществующего ключа должно возвращаться None"

def test_update_value():
    updated_dict = periodic_table.copy()
    updated_dict[1] = {"name": "Hydrogen", "symbol": "H", "atomic_mass": 1.5}
    assert dictionariesSets.update_value(periodic_table.copy(), 1, {"name": "Hydrogen", "symbol": "H", "atomic_mass": 1.5}) == updated_dict, "Значение ключа 1 должно обновиться"
    assert dictionariesSets.update_value(periodic_table.copy(), 21, {"name": "Unknown"}) is None, "Для несуществующего ключа должно возвращаться None"

def test_delete_entry():
    test_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
    assert dictionariesSets.delete_entry(test_dict, 2) == {1: 'a', 3: 'c', 4: 'd'}, "Запись с ключом 2 должна быть удалена"
    assert dictionariesSets.delete_entry(test_dict, 5) == test_dict, "Если ключ не существует, словарь не должен изменяться"

def test_get_keys():
    test_dict = {"1class": "xbyxby", "2class": "xoxioix", "3class": "sdsd"}
    assert dictionariesSets.get_keys(test_dict) == ["1class", "2class", "3class"], "верный список ключей"

def test_create_set():
    assert dictionariesSets.create_set([1, 2, 3, 4, 5, 5, 5]) == [1, 2, 3, 4, 5], "Множество должно содержать уникальные элементы"
    assert dictionariesSets.create_set([1, 1, 3, 5, 3, 2, 1]) == [1, 3, 5, 2], "Множество должно содержать уникальные элементы"

def test_union_sets():
    assert dictionariesSets.union_sets([1, 2, 3], [3, 1, 5]) == [1, 2, 5, 3], "Объединение должно содержать элементы из обоих множеств"
    assert dictionariesSets.union_sets([7, 5, 3, 4], [3, 1, 5]) == [7, 5, 3, 1, 4], "Объединение должно содержать элементы из обоих множеств"

def test_intersection_sets():
    assert dictionariesSets.intersection_sets([1, 2, 3], [3, 2, 5]) == [3, 2], "Пересечение должно содержать только общие элементы"
    assert dictionariesSets.intersection_sets([3], [3, 2, 5]) == [3], "Пересечение должно содержать только общие элементы"

def test_difference_sets():
    assert dictionariesSets.difference_sets([1, 2, 3, 7], [3, 2, 5, 4]) == [1, 7], "Разность должна содержать только уникальные элементы первого множества"
    assert dictionariesSets.difference_sets([3, 7], [3, 2, 5, 7]) == [], "Разность должна содержать только уникальные элементы первого множества"

def test_is_element_in_set():
    assert dictionariesSets.is_element_in_set([1, 2, 3, 7], 2) == True, "Элемент 2 должен находиться в множестве"
    assert dictionariesSets.is_element_in_set([1, 2, 3, 7], 5) == False, "Элемент 5 не должен находиться в множестве"

run_test(test_create_dict)
run_test(test_get_value)
run_test(test_update_value)
run_test(test_delete_entry)
run_test(test_get_keys)
run_test(test_create_set)
run_test(test_union_sets)
run_test(test_intersection_sets)
run_test(test_difference_sets)
run_test(test_is_element_in_set)

if sum(test_res) == 0:
    print("0%")
else:    
    print("Тест пройден на " f"{int(len(test_res)/sum(test_res))*100}%")
