def create_dict(keys: list, values: list) -> list:
    dictionaries = {}
    if(len(keys) == len(values)):
        for i in range(len(keys)):
            dictionaries[keys[i]] = values[i]

    return dictionaries

#print(create_dict([1,2,3,4],["a","b",'c','d']))

def get_value(dictionary: dict, key: any) -> any:
    for item in dictionary:
        if(item == key):
            return dictionary[item]
        else: 
            return None


#print(get_value({1: 'a', 2: 'b', 3: 'c', 4: 'd'},1))
#print("########")
def update_value(dictionary: dict, key: any, new_value: any) -> dict:
    for item in dictionary:
        print(item)
        if(item == key):
            dictionary[item] = new_value
            return dictionary
        else: 
            return None



#print(update_value({1: 'a', 2: 'b', 3: 'c', 4: 'd'},1,"7761232176783"))

def delete_entry(dictionary: dict, key: any) -> dict:
    diction = {}
    for item in dictionary:
        if(item == key):
            continue
        diction[item] = dictionary[item]
        
        
    return diction

        
#print(delete_entry({1: 'a', 2: 'b', 3: 'c', 4: 'd'},2))

def get_keys(dictionary: dict) -> list:
    keyArray = []
    for item in dictionary:
        keyArray.append(item)
    return keyArray

print(get_keys({"1class":"xbyxby","2class":"xoxioix","3class":'sdsd'}))


def create_set(lst: list) -> list:
    sett = []
    # for i in lst:
        
    # return sett
print(create_set([1,2,3,4,5,5,5]))