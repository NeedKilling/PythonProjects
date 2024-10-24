def create_dict(keys: list, values: list) -> list:
    dictionaries = {}
    if(len(keys) == len(values)):
        for i in range(len(keys)):
            dictionaries[keys[i]] = values[i]

    return dictionaries

def get_value(dictionary: dict, key: any) -> any:
    for item in dictionary:
        if(item == key):
            return dictionary[item]
        else: 
            return None

def update_value(dictionary: dict, key: any, new_value: any) -> dict:
    for item in dictionary:
        print(item)
        if(item == key):
            dictionary[item] = new_value
            return dictionary
        else: 
            return None

def delete_entry(dictionary: dict, key: any) -> dict:
    diction = {}
    for item in dictionary:
        if(item == key):
            continue
        diction[item] = dictionary[item]     
    return diction

def get_keys(dictionary: dict) -> list:
    keyArray = []
    for item in dictionary:
        keyArray.append(item)
    return keyArray

def create_set(lst: list) -> list:
    sett = []
    for i in lst:
        if i not in sett:
            sett.append(i)
    return sett

def union_sets(set1: list, set2: list) -> list:
    sets = []
    for i in range(len(set1)):
        if(i == len(set1)-1):
            for j in set2:
                if j not in set1:
                    sets.append(j)
        sets.append(set1[i])
    return sets

def intersection_sets(set1: list, set2: list) -> list:
    sets = []
    intersection = []
    for i in range(len(set1)):
        if(i == len(set1)-1):
            for j in set2:
                if j in set1:
                    intersection.append(j)
        sets.append(set1[i])
    return intersection

def difference_sets(set1: list, set2: list) -> list:
    sets = []
    for i in set1:
        if i not in set2:
            sets.append(i)
    return sets

def is_element_in_set(set1: list, element: any) -> bool:
    for i in set1:
        if element in set1:
            return True
        else:
            return False

 