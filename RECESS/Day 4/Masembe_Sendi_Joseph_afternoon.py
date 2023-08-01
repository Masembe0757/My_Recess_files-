#Function
def Print():
    print("Hello evening")
Print()
def Sum(a,b):
    return a*b
result = Sum(7,3)
print("The sum of 7 and 3 is ",result)

def multiply_all(*args):
    prod = 1
    for x in args :
        prod *= x
    return prod
result1 = multiply_all(1,2,3,5)
print("Product of all arguments is ",result1)

import Div  # or from Div import Divide
print("The result of 30/2 is",Div.Divide(30,2))

from math import sqrt 
print("The square root of 49 is ",sqrt(49)) 

#User input and output
age = int(input("Enter your age:"))
if age < 0:
    print("Age can not be negative value")
else:
    print("Age ",age," saved successfully")
    
#Multiple input => same data type
name , village = map(str, input("Enter fields name and village").split())
print("The values are ", end= " ")
print(name, " is from ",village)
