
#WORK TO STRING

def count_characters(text: str) -> int: 
    count = 0
    for i in text:
        count += 1
    return count
#print(count_characters("alalla"))


def	reverse_string(text: str) -> str:
    textArr = ""
    for j in range(count_characters(text)-1,-1,-1):
        textArr += text[j]
    return textArr

#print(reverse_string("hello"))

def to_upper(text: str) -> str:
    pass

def to_upper(text: str) -> str:
    pass


def capitalize_string(text: str) -> str:
    pass


def count_words(text: str) -> int: 
    textArr = text.split()
    count = 0
    for i in textArr:
        count+=1

    return count
print(count_words("helloo alo hell")," words")


#WORK TO LIST

def count_list(lst: list) -> int: 
    count = 0
    for i in lst:
        count += 1
    return count

def find_minimum(lst: list) -> float: 
    
    min = lst[0]
    for i in range(0,count_list(lst)):
        if(min > lst[i]):
            min = lst[i]
            
    return min

print(find_minimum([1,2,3,4,5]))


def find_maximum(lst: list) -> float: 
    max = lst[0]
    for i in range(0,count_list(lst)):
        if(max < lst[i]):
            max = lst[i]        
    return max

print(find_maximum([1,2,3,4,5]))

def sort_ascending(lst: list) -> list:
    min = 0
    max = lst[count_list(lst)-1]
    lstArr = []

    for i in range(0,count_list(lst)):
        if(min < lst[i]):
            min = lst[i]
            lstArr.append(min)


    return lstArr

print(sort_ascending([3,4,2,1,5]))