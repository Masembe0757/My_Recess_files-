def Morning():
    #Single line comment
    """This is a function
       for my morning session.
        """
        #Snake case is more preferred for python programmers such as google_developers_team
        #camelCase
        #PascalCasE
    my_name = "Masembe Sendi Joseph"
    my_age = 19
    print("My name is ", my_name," and Im aged ",my_age)
    

Morning()


print()
print()

def Afternoon() :
    """This is a function
       for my afternoon session.
        """
    print(type(4))
    print(type("Helo"))
    print(type(True))
    print(type(5j))
    
    #LISTS => ordered and allow duplicate values
    
    names = ["James", "Akward","Alfred","Mikaelson","Klaus","James"]
    print (names)
    print("There are ",len(names)," members in names list")
    print(names[0], "is at index 0")
    print(names[-2], "is at index 4 / -2")
    print(names[3:5], "is between 3(inclusive) and 5 (exclusive) ")
    print(names[1:], "is from index 1 to end of the list ")
    names.remove("Akward")
    print(names," Has no Akward") 
    names.pop(2)
    print(names,"Has element previously at index 2 removed")
    names.insert(0,"Harward")
    print(names,"Has Harward at index zero") 
    names.append("Dauglous")
    print(names, "Has Dauglous added at end of list")
    print()
    print()
    
    #TUPLES =>Ordered and immutable
    Cars = ("Limo","Surf","Mazda","Forester","Sienta")
    print(Cars)
    
    #Exercise
    print("Tuple has",len(Cars)," Cars")
    #Multiple type tuple
    Guns_and_bullets = ("Revolver",67,"Short-Gun",56,"Gauge-millimeter",45)
    
    print(Guns_and_bullets)
    
    #Accessing a tuple member
    print(Guns_and_bullets[0]," is the first gun on the tuple of guns")
    
    #Altering a tuple => first changing it to a mutable data type such as a list
    mutable_Cars = list(Cars)
    mutable_Cars.append("Benz")
    Cars = tuple(mutable_Cars)
    print(Cars)
    print()
    
    #Adding two tuples
    Fruits_A = ("Berries","Orchards","Tomatoes")
    Fruits_B =("Guava","Straw Berry")
    
    # For a single item tuple use a trailing comma
    Fruits_C = ("Apple",)
    Fruits_B += Fruits_C
    Fruits_A += Fruits_B
    print(Fruits_A)
    
    print()
    print()
    
    #SETS => No duplication
    male_names = {"John","Livingstone","Arnold","Arnold"}
    sur_names = {"Steven","Jackson"}
    print(male_names) #prints single Arnold
    
    #Exercise length, datatype, Accessing, add items, append two sets
    
    print("This set has ",len(male_names)," members")
    print(type(male_names))
    print()
    
    #Accessing elements of a set
    print("Elemets in a male_names set")
    for i in male_names:
        print (i)
        
    #Adding an item
    male_names.add("Joseph")
    print(male_names)
    
    #Joining sets
    united_sets =  male_names.union(sur_names)
    print(united_sets)
    
    
    
Afternoon()
