def Morning():
    #Dictionaries => Used to store data in form key and value pairs and like sets do not allow duplicates
    spouses = {"Anna":"Joseph","Marry":"Jackson","Edith":"Jacob"}
    
    #Entering the same old key with new value overrites the previous value
    print(spouses)
    print("Spouses doctinary has ",len(spouses)," pairs")
    print("Anna is married to ",spouses["Anna"])
    
    #Using the dictionary constructor
    dict_A = dict(Daniel= 56,Phillip= 67,dell = "hp")
    print(dict_A)
    
    #A programme to check mental health using dictionaries.
    
    
    mental_health_dictiomary = {
        "headache":"This can be caused by over working without rest, u could take a nap",
        "sleepless":"This is a condition called insomnia caused by overthinking, have some time out",
        "well": "Good progress!",
        "puzzled":"Take sometime off the problem's environment"} 
    
    #User input either input() or raw_input() depending on python version
    
    feeling = input("How are you feeling right now ?")
    if feeling in mental_health_dictiomary :
        response = mental_health_dictiomary[feeling]
        print(response)
    else :
        print("Sorrry we dont have the help you need")
        
        
         
    #ARRAYS => The are more like lists and operations on them return a copy of lists
    Teams = ["Bayern","Arsenal","Liverpool","Manchester","Man-united"]
    print(Teams)
    print(len(Teams))
    
    #CONDITIONAL STATEMENTS
    age = 18
    if(age<18) :
        print("Person is an infant")
    elif(age>=18 and age<=45) :
        print("Person is a youth")
    else :
        print("Person is an adult")
        
    #LOOPS
    # for loop, while loop, do while loop
    cars = ("cardigan","skoda","limo","bmw")
    
    for x in cars: 
        print (x)
        
    Inmates = ["deno","Fogus","Disaster","plague","snoot"]
    count = 0
    print()
    while count <len(Inmates):
        print(Inmates[count])
        count += 1   
        
        print() 
        num = 0
    while num < 10 :
        if num in range(2,8):
            print(num)
        num += 1
        
    #skipping number 5 using continue
    #continue => continuing with a loop even when condition is false
    print()
    print("skipping number 5 using continue")
    numbers = [1,2,3,4,5,6,7,8,9,10]
    for x in numbers :
        
        if x == 5 :
            continue
        
        print(x)
        
        
    #stopping at 5 using break
    #break => jumping out of a loop even when condition holds
    print()
    print("stopping at 5 using break")
    for x in numbers :
        print(x)
        if x==5 :
            break
        
        
    #EXCEPTION HANDLING
    
    try:
        x= 5
        y= 0
        print(x/y)
    except:
        print("Zero devisors not allowed")
    finally:
        print("Block execution done")
    
    '''
ITERATORS
an iterator is an object that contains 
countable number of values and it can be traversed through. Iterable objects include;
lists,tuples, sets, dictionaries. It can also be a String of characters

it contains methods such as  __iter__() and __next__()
'''
#Using a list
letters = ["A","B","C","D","E"]
items = iter(letters)
print(next(items))
print(next(items))
print(next(items))
print(next(items))


#Object Oriented Pyhton Classes , objects and inheritance
        
        
        
Morning()
print()
print()
def Afternoon() :
    #DICTIONARY EXERCISE

    vehicle_horsepower ={"jaguar":450,"Dodger":500,"Hammer":700,"Benz":650,"Wagon":750}
    
    #Using values() method
    horse_powers = vehicle_horsepower.values()
    print(horse_powers)  
    
    #Checking if key exists in the dictionary
    key = "jaguar"
    if key in vehicle_horsepower :
        print("Key ",key," exists in the dictionary")
    else:
        print("Key not part of the dictioary")
    
    #Updating a dictionary, Changing a value and adding new pairs
    vehicle_horsepower.update({"Forester":9700})
    vehicle_horsepower.update({"jaguar":978}) #Changing value of jaguar horse power to 978 by overriting
    print(vehicle_horsepower) #now with forester : 9700 pair and 978 jaguar
    
    #Removing a pair
    vehicle_horsepower.pop("Hammer")
    print(vehicle_horsepower) #without hammer : 700 pair
    
    #looping through a dictionary
    for x in vehicle_horsepower:
        print("The car ",x," has horsepower ",vehicle_horsepower[x])
    
    #Nesting Dictionaries
    reds ={"red_apple": 1000,"red_mago":500}
    fruit_cost = {"pears":1000,"strawberry":1500,"Red_fruits":reds}
    
    #print price of a red app apple
    print("The sprice of red apple is ",fruit_cost["Red_fruits"]["red_apple"])
    
    # DATA TYPES
a = 2  # int
b = 6j  # complex
c = 6.5557  # float


# EXERCISE, type conversion
# float to complex
z = complex(c)
print(type(z))
# int to float
x = float(a)
print(type(x))

# complex to float
#r = float(b) impossible since float coversino must be a real number or string

#STRINGS
name = "Joseph"
print(name)

#single line string
gender= "male"

'''Assignment
use the len() method for length
use a for loop
an example in slicing in strings
'''
print ("String male has ",len(gender)," characters")

for y in gender:
    print(y)
    
# Slicing example in strings

Trueth = "The world is a better place"

# Slicing a string
slice1 = Trueth[0:9]  # Slice from index 0 to 9 (exclusive)
slice2 = Trueth[4:]   # Slice from index 4 to the end
slice3 = Trueth[:10]   # Slice from the beginning to index 10 (exclusive)
slice4 = Trueth[::4]  # Slice with step-size of 4

print("Slice 1:", slice1)
print("Slice 2:", slice2)
print("Slice 3:", slice3)
print("Slice 4:", slice4)

#multiline strings
StrA = '''Weekends dont last for so long'''
 
 # string as an array
drug = "Heroin"
for x in drug:
    print(x)
      
#EXERCISE
#modifying a string
strB="sandman" 
print(strB.upper())
strC ="HEADACHE"
print(strC.lower())

strD = "     Angels         "
print(strD.strip()) #Removes leading and trailing spaces
 
#string concatenation
he = "super"
ro = "man"
print (he+" "+ro)

#formating strings
name = "Joseph"
occupation = "front-end developer"
age = 19


# Using positional arguments
about1 = "My name is {}. I'm {} years old and I work as an {}.".format(name, age, occupation)
print(about1)

# Using indexed arguments
about2= "My name is {0}. I'm {1} years old and I work as a {2}.".format(name, age, occupation)
print(about2)

# Using named arguments
about3 = "My name is {a}. I'm {b} years old and I work as a {c}.".format(a=name, b=age, c=occupation)
print(about3)

# Using f-strings (Python 3.6+)
about4 = f"My name is {name}. I'm {age} years old and I work as a {occupation}."
print(about4)


#booleans return either true or false
#mainly used on blocks executed according to a condition
numk = 10
 
if(numk>50):
    print("false")   
else :
    print("true")
    
Afternoon()

def Test() :
    pass #used to skip a block that has no statements in it.