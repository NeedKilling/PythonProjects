def find_minimum(lst: list) -> float:
    min = lst[0]
    for i in range(0, len(lst)):
        if lst[i] < min:
            min = lst[i]
    return min

def find_maximum(lst: list) -> float:
    max = lst[0]
    for i in range(0, len(lst)):
        if lst[i] > max:
            max = lst[i]
    return max

def sort_ascending(lst: list) -> list:
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def sort_descending(lst: list) -> list:
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def average(lst: list) -> float:
    sum = 0
    count = 0
    for i in lst:
        sum+=i
        count+=1
    return sum/count

def remove_duplicates(lst: list) -> list:
    sorted_list = sort_ascending(lst)
    new_list = [sorted_list[0]]
    for i in range(1, len(sorted_list)):
        if sorted_list[i] != sorted_list[i-1]:
            new_list.append(sorted_list[i])
    
    return new_list

def find_median(lst: list) -> float:
    sorted_list = sort_ascending(lst)
    length = len(sorted_list)
    if (length%2 != 0):
        median = sorted_list[length//2]
    else:
        print(sorted_list[length//2])
        print(sorted_list[length//2+1])
        median = (sorted_list[length//2 - 1] + sorted_list[length//2]) / 2
    return median

def is_sorted(lst: list) -> bool:
    currentList = [] + lst
    sort_ascending(lst)
    for i in range(0,len(lst)):
        if lst[i] == currentList[i]:
            continue
        else: return False
    return True

def reverse_list(lst: list) -> list:
    new_list = []
    for i in range(len(lst) - 1, -1, -1):
        new_list.append(lst[i])
    return new_list

def count_frequency(lst: list) -> dict:
    freq_dict = {}
    for element in lst:
        if element in freq_dict:
            freq_dict[element] += 1
        else:
            freq_dict[element] = 1
    return freq_dict

