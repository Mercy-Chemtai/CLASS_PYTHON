def hello(name):
    print(f"Hello {name}")

def year_of_birth(name,age):
    print(f"Hello {name},you were born in {2024-age}")
   
def my_country(country="Uganda"):
    print(f"Hello Akirachix from {country}" )

def greet(*names):
    for name in names
    print(f"Hello {names}")















#
n = 5
d=dict()
for x in range(1,n+1):
    d[x] = x*x
print(d)

#or
l=[1,2,3,4]
squares={x:x*x for x in l}
print(squares)



def check_anagram(str1,str2):
    sorted_str1 = str1.lower()
    sorted_str2 = str2.lower()
    
    if sorted_str1 == sorted_str2:
        print(f"${sorted_str1} and ${sorted_str2} are anagrams")
    else:
        print(f"${sorted_str1} and ${sorted_str2} are not anagrams")  

str1= "god"
str2= "dog"
check_anagram(str1,str2) 


#reversing a string
def reverse_string(str):
    print(str[::-1])

str = "mercy" 
reverse_string(str)   


#counting the vowels
def count_vowel(str):
    count = 0
    vowels = set("a,e,i,o,u,A,E,I,O,U")
    for alphabet in vowels:
        if alphabet in vowels:
            print (alphabet.count("str"))
        else:
            print(alphabet.count("str"))

str = "mercy"
count_vowel(str)  
#or
def my_vowels(name,vowels):
    count=sum(name.count(vowel)for vowel in vowels)
    print(count) 
name = "mercy"
vowels = "aeiouAEIOU"
my_vowels(name,vowels)             


        

