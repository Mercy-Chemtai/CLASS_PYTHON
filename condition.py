def print_numbers(n):
    numbers = range(n)
    for number in numbers:
        print(number)

print_numbers(5)        

def print_even_numbers(n):
    numbers = range(n)
    for number in numbers:
        if number%2 == 0:
          print(f"{number} is an even number")
        else:
            print(f"{number} is not an even number")


print_even_numbers(10)


def check_divisibility(n):
    numbers = range(n)
    for number in numbers:
        if number%3 == 0:
            print(f"{number} is divisible by 3")

        elif number%5 == 0:
            print(f"{number} is divisible by 5")

        elif number%7 == 0:
            print(f"{number} is divisible by 7")  

        else:
            print(f"{number} is not divisible by 3,5 or 7")   


check_divisibility(100) 


def count_down(n):
    x=0
    while n>x:
        print(n)
        n-=1

count_down(10)  

def count_down_to_five(n):
    x=0
    while n>x:
        if n == 5:
            break
            print(n)
        n-=1
        
                
count_down_to_five(10) 


def divisible_by_seven(n):
    x=1
    while x<n:
        x+=1
        if x%7 != 0:
            continue
            print(f"{x} is divisible by 7")

divisible_by_seven(10)       

#Using while , continue and if statements, write a function that prints all the odd numbers between 0 and 100

def odd_numbers():
    x=0
    while x<100:
        x+=1
        if x%2 ==0:
           continue
           print(f"{x} is a odd number")

odd_numbers()           


#Create a function named fizzbuzz. - For numbers divisible by 3 it prints fizz - for numbers divisible by 5 it prints buzz 
#- for all the numbers it prints fizzbuzz use if,elif,else.

def fizzbuzz(numbers):
    number= 1
    while number<numbers:
        if number%3 == 0:
            print("fizz")
        elif numbers%5 ==0
             print("buzz")
        else:
            print("fizzbuzz")






        