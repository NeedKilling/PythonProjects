#import rows_lib
import stringsAndLists_lib
test_res = []

def run_test(test_fanc):
    try:
        test_fanc()
        test_res.append(True)    
    except:     
        print(f"{test_fanc.__name__} faled")
        test_res.append(False)   

def test_int_add_float():
    # assert stringsAndLists_lib.math_lib.int_add_float(5,3.2) == 5 + 3.2, "5 + 3.2 должно быть 8.2"
    # assert stringsAndLists_lib.math_lib.int_add_float(-5,3.2) == -5 + 3.2, "-5 + 3.2 должно быть -1.8"
    # assert stringsAndLists_lib.math_lib.int_add_float(5,-3.2) == 5 + (-3.2), "5 + (-3.2) должно быть 1.8"
    pass

# def test_count_characters():
#     assert stringsAndLists_lib.rows_lib.count_characters("hello") == 5, "5"
#     pass

def test_count_characters():
    assert stringsAndLists_lib.count_characters("Hello") == 5, "Количество символов в 'Hello' должно быть 5"
    assert stringsAndLists_lib.count_characters("") == 0, "Количество символов в пустой строке должно быть 0"
    assert stringsAndLists_lib.count_characters(" ") == 1, "Количество символов в строке с пробелом должно быть 1"

def test_reverse_string():
    assert stringsAndLists_lib.reverse_string("Hello") == "olleH", "Перевернутая строка 'Hello' должна быть 'olleH'"
    assert stringsAndLists_lib.reverse_string(" ") == " ", "Перевернутая строка с пробелом должна быть ' '"
    assert stringsAndLists_lib.reverse_string("") is None, "Перевернутая пустая строка должна вернуть None"

def test_to_upper():
    assert stringsAndLists_lib.to_upper("hello") == "HELLO", "Строка 'hello' должна преобразоваться в 'HELLO'"
    assert stringsAndLists_lib.to_upper("HELLO") == "HELLO", "Строка 'HELLO' должна остаться 'HELLO'"
    assert stringsAndLists_lib.to_upper("Hello World!") == "HELLO WORLD!", "Смешанная строка должна стать верхним регистром"

def test_to_lower():
    assert stringsAndLists_lib.to_lower("HELLO") == "hello", "Строка 'HELLO' должна преобразоваться в 'hello'"
    assert stringsAndLists_lib.to_lower("hello") == "hello", "Строка 'hello' должна остаться 'hello'"
    assert stringsAndLists_lib.to_lower("Hello World!") == "hello world!", "Смешанная строка должна стать нижним регистром"

def test_capitalize_string():
    assert stringsAndLists_lib.capitalize_string("hello") == "Hello", "Строка 'hello' должна стать 'Hello'"

def test_remove_extra_spaces():
    assert stringsAndLists_lib.remove_extra_spaces("Hello") == "Hello", "Строка без лишних пробелов должна остаться 'Hello'"
   
def test_is_palindrome():
    assert stringsAndLists_lib.is_palindrome("racecar") is True, "Слово 'racecar' является палиндромом"
    assert stringsAndLists_lib.is_palindrome("hello") is False, "Слово 'hello' не является палиндромом"

def test_count_words():
    assert stringsAndLists_lib.count_words("Hello World") == 2, "В строке 'Hello World' должно быть 2 слова"
    assert stringsAndLists_lib.count_words("") == 0, "Пустая строка должна иметь 0 слов"

def test_replace_substring():
    assert stringsAndLists_lib.replace_substring("Hello World", "World", "Universe") == "Hello Universe", "Замена 'World' на 'Universe'"
    assert stringsAndLists_lib.replace_substring("ababab", "ab", "cd") == "cdcdcd", "Замена 'ab' на 'cd'"

def test_remove_digits():
    assert stringsAndLists_lib.remove_digits("123Hello456") == "Hello", "Все цифры должны быть удалены из строки"
    assert stringsAndLists_lib.remove_digits("NoDigits") == "NoDigits", "Строка без цифр должна остаться неизменной"
def test_find_minimum():
    assert stringsAndLists_lib.find_minimum([4, 2, 3, 1]) == 1, "Минимум в [4, 2, 3, 1] должен быть 1"
    assert stringsAndLists_lib.find_minimum([10, 5, 7, 3]) == 3, "Минимум в [10, 5, 7, 3] должен быть 3"

def test_find_maximum():
    assert stringsAndLists_lib.find_maximum([4, 2, 3, 1]) == 4, "Максимум в [4, 2, 3, 1] должен быть 4"
    assert stringsAndLists_lib.find_maximum([10, 5, 7, 3]) == 10, "Максимум в [10, 5, 7, 3] должен быть 10"

def test_sort_ascending():
    assert stringsAndLists_lib.sort_ascending([4, 2, 3, 1]) == [1, 2, 3, 4], "Список должен быть отсортирован по возрастанию"
    assert stringsAndLists_lib.sort_ascending([10, 5, 7, 3]) == [3, 5, 7, 10], "Список должен быть отсортирован по возрастанию"

def test_sort_descending():
    assert stringsAndLists_lib.sort_descending([4, 2, 3, 1]) == [4, 3, 2, 1], "Список должен быть отсортирован по убыванию"
    assert stringsAndLists_lib.sort_descending([10, 5, 7, 3]) == [10, 7, 5, 3], "Список должен быть отсортирован по убыванию"

def test_average():
    assert stringsAndLists_lib.average([4, 2, 3, 1]) == 2.5, "Среднее значение в [4, 2, 3, 1] должно быть 2.5"
    assert stringsAndLists_lib.average([10, 5, 7, 3]) == 6.25, "Среднее значение в [10, 5, 7, 3] должно быть 6.25"

def test_remove_duplicates():
    assert stringsAndLists_lib.remove_duplicates([1, 2, 2, 3, 4, 4]) == [1, 2, 3, 4], "Дубликаты должны быть удалены"
    assert stringsAndLists_lib.remove_duplicates([1, 1, 1, 1]) == [1], "Все дубликаты должны быть удалены"

def test_find_median():
    assert stringsAndLists_lib.find_median([4, 2, 3, 1]) == 2.5, "Медиана в [4, 2, 3, 1] должна быть 2.5"
    assert stringsAndLists_lib.find_median([10, 5, 7]) == 7, "Медиана в [10, 5, 7] должна быть 7"

def test_is_sorted():
    assert stringsAndLists_lib.is_sorted([1, 2, 3, 4]) is True, "Список [1, 2, 3, 4] должен быть отсортирован"
    assert stringsAndLists_lib.is_sorted([4, 3, 2, 1]) is False, "Список [4, 3, 2, 1] не должен быть отсортирован"

def test_reverse_list():
    assert stringsAndLists_lib.reverse_list([1, 2, 3]) == [3, 2, 1], "Список [1, 2, 3] должен быть перевернут"
    assert stringsAndLists_lib.reverse_list([]) == [], "Пустой список должен остаться пустым"

def test_count_frequency():
    assert stringsAndLists_lib.count_frequency([1, 2, 2, 3]) == {1: 1, 2: 2, 3: 1}, "Частота элементов должна быть правильной"
    assert stringsAndLists_lib.count_frequency([]) == {}, "Частота элементов в пустом списке должна быть пустым словарем"




run_test(test_int_add_float)
run_test(test_count_characters)
run_test(test_reverse_string)
run_test(test_to_upper)
run_test(test_to_lower)
run_test(test_capitalize_string)
run_test(test_remove_extra_spaces)
run_test(test_is_palindrome)
run_test(test_count_words)
run_test(test_replace_substring)
run_test(test_remove_digits)
run_test(test_find_minimum)
run_test(test_find_maximum)
run_test(test_sort_ascending)
run_test(test_sort_descending)
run_test(test_average)
run_test(test_remove_duplicates)
run_test(test_find_median)
run_test(test_is_sorted)
run_test(test_reverse_list)
run_test(test_count_frequency)


if sum(test_res) == 0:
    print("0%")
else:    
    print("Тест пройден на "f"{int(len(test_res)/sum(test_res))*100}%")
