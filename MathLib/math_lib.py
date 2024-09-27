def int_add_float(int_number:int, float_number:float) ->float:
    return int_number + float_number

def int_substract_float(int_number:int, float_number:float) ->float:
    return int_number - float_number

def multiply_numbers(int_number:int, float_number:float) ->float:
    return int_number * float_number

def devide_numbers(numl:float,num2:float) -> float:
    if num2 != 0:
        return numl / num2
    else: "error0"
       
def is_even(number:int) -> bool: 
    if isinstance(number,int):
        if (number % 2) == 0:
            return True
        else: 
            return False
    else:
        return "errorType"
    
def factorial(number:int)->int:
    count = 1
    for i in range(1,number+1):
        count *= i
    return count

def sin_approximation(x:float,epsilon:float)->float:
    counter = 0
    sinX = x
    pow = 3
    while True:
        counter+=1
        funct = (x**pow)/factorial(pow)
        if(funct>epsilon):    
            if(counter % 2) == 0:
                sinX += funct
            else: 
                sinX -= funct
            pow += 2
        else:
            return sinX
     
def cos_approximation(x:float,epsilon:float)->float:
    counter = 0
    cosX = 1
    pow = 2
    while True:
        counter+=1
        funct = (x**pow)/factorial(pow)
        if(funct>epsilon):    
            if(counter % 2) != 0:
                cosX -= funct
            else: 
                cosX += funct
            pow += 2
        else:
            return cosX


def custom_ceil(number:float) -> int:

    if ( number % 1 != 0 ):
        return int(number//1 + 1)
    else:
        return int(number) + 1
    

    
def custom_floor(number:float) -> int:
    if (number < 0):
        return int(number) - 1
    else:
        return int(number) 
    
