def add(x,y):
    result=x+y
    return result

answer = add(1000,2000)
print(answer)

def subtract(x,y):
    result= y-x
    return result

answer=subtract(2000,1000)
print(answer)

def divide(y,x):
    result= y/x
    return result

answer= divide(50,2)
print(answer) 

def multiply(y,x):
    result= y*x
    return result

answer= multiply(50,2)
print(answer)  

def remainder(y,x):
    result= y%x
    return result

answer= remainder(100,30)
print(answer) 

def power_of(x,y):
    result= x**y
    return result

answer= power_of(2,3)
print(answer)  

def sum(*numbers):
    total = 0
    for number in numbers:
        total+=number
    return total 

def multiply_many(*numbers):
    total = 1
    for number in numbers:
        total*=number
    return total    

def create_sentence(**words):
    sentence = " "
    for word in words:
        sentence+=word 
        sentence+=" "   
    return sentence  

def sum_and_greet(*args,**Kwargs):
    total = 0 
    for x in args:
       total+= x

    p = Kwargs['first_name']
    l = Kwargs['last_name']
    greeting = f"Hello {p} {l} the sum of your numbers is {total}"
    return greeting         

       
