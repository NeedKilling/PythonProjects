def count_characters(text: str) -> int:
    if text != "":
        count = 0
        for letter in text:
            count = count+1
        return count
    else: return 0

def reverse_string(text: str) -> str:
    if text != "":
        s = ""
        for letter in text:
            s = letter + s
        return s

def to_upper(text: str) -> str:
    if text != "":
        s = ""
        for letter in text:
            code = ord(letter)
            if code <= 92:
                s+=letter
            else: s+=chr(code - 32)
        return s

def to_lower(text: str) -> str:
    if text != "":
        s = ""
        for letter in text:
            code = ord(letter)
            if code < 97 and code >= 65:
                s+=chr(code + 32)
            else: s+=letter
        return s

def capitalize_string(text: str) -> str:
    if text != "":
        if ord(text[0]) > 92:
            return chr(ord(text[0]) - 32) + text[1:]

def remove_extra_spaces(text: str) -> str:
    if text != "":
        s = ""
        lastChar = ''
        if text[0] == ' ': text = text[1:]
        if text[-1] == ' ': text = text[:-1]
        for ch in text:
            if ch == ' ' and ch == lastChar:
                s = s
            else:
                s+=ch
            lastChar = ch
        return s

def is_palindrome(text: str) -> bool:
    if text != "":
        if text == reverse_string(text):
            return True
        else: 
            return False
    
def count_words(text: str) -> int:
    if text != "":
        text = remove_extra_spaces(text)
        count = 1
        for ch in text:
            if ch == ' ':
                count+=1
        return count
    else: return 0


def replace_substring(text,old,new):
    if text != "":
        s=""
        skip = 0 
        skiptimes = count_characters(new) -1 
        if old in text:
            for i in range(0, count_characters(text)):
                if skiptimes > 0 and skip == 1: 
                    skiptimes -= 1
                    if skiptimes == 0:
                        skip = 0 
                        skiptimes = count_characters(new) -1 
                    continue
                else: 
                    if text[i:i+count_characters(old)]==old:
                        s=s+new
                        skip = 1
                    else:
                        s=s+text[i]
    return s


def remove_digits(text: str) -> str:
    if text != "":
        s = ""
        for ch in text:
            if (48<= ord(ch) <= 57):
                s = s
            else: s+=ch
        s = remove_extra_spaces(s)
        return s
    

    

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

