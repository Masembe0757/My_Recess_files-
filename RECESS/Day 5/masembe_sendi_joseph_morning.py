#INHERITANCE

class AutoMobile:
    def __init__(self,name,brand,type):
        self.name = name
        self.brand = brand
        self.type = type
        
    def move(self):
        print("Auto mobile is moving")
        
    def info(self):
        print("name ",self.name)
        print("brand ",self.brand)
        print("type ",self.type)
class Motocycle(AutoMobile):
    def __init__(self,name,cost,color):
        self.cost = cost
        self.color = color
        self.name = name
        
    def honk(self):
        print(self.name," is honking")
        
    def details(self):
        print("name ",self.name)
        print("cost ",self.cost)
        print("color ",self.color)
        
mt_one = Motocycle("Bajaj",6000000,"blue")
mt_one.details()
mt_one.honk()
mt_one.move()




#ASSIGNMENT  ONE    
# Using inher calculate paremeter and area of a rectangle and circle respectively
class shape:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def add_sides(self,x,y):
        return x+y
    def square_sides(self,p):
        return p*p
class Rectangle(shape):
    def __init__(self, length, width):
        super().__init__(length, width)
    def Rect_perimeter(self):
        print("The perimeter of the rectangle is ",2*super().add_sides(self.length,self.width)," units")    
    
class Circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def Circle_perimeter(self):
        print("The area of a circle is ",3.14*super().square_sides(self.radius)," square units")
        
print()
        
rect_one = Rectangle(2,2)
circle_one = Circle(2)
rect_one.Rect_perimeter()
circle_one.Circle_perimeter()

print()



#POLYMORPHISM
#Ability of a method to exist with different implemetation
#THROUGH METHOD OVERIDING
class Animal:
    def __init__(self,name) :
        self.name = name
    def Run(self):
        print("All animals can run")
class WildAnimal(Animal):
    #by overriding the Run method of the parent class, we are creating its other
    # different form though similar name and doing different functions
    def Run(self):
        print(self.name," runs faster than leopards")
class DomesticAnimal(Animal):
    def Run(self):
        print(self.name," runs moderately")
        
def Individual_run(Animal):
        Animal.Run()
        
animal_one = WildAnimal("Deer")
animal_two = Animal("Tiger")
home_animal = DomesticAnimal("Cow")
home_animal.Run()
animal_two.Run()
animal_one.Run()

#OR   by invoking Individual_run method
print()
Individual_run(home_animal)


#THROUGH OVERLOADING
def subtract(x,y):
    return x+y
def subtract(x,y,z):
    return x+y+z


#ABSTRACTION
#allows to focus on essential features and hide unnecessary details
from abc import ABC , abstractmethod
class Staff(ABC):
    @abstractmethod
    def purpose(self):
        pass
class Manager(Staff):
    def purpose(self):
        print("Manager pays salary")
class Cleaner(Staff):
    def purpose(self):
        print("Cleaners clean litter")
        
mn_one = Manager()
mn_two = Cleaner()
print()
mn_two.purpose()
mn_one.purpose()


#ASSIGNMENT TWO
#Using abstraction, calculate area and parameter of a circle and rectangle respectively

class shape(ABC):
    def __init__(self,length,width):
        self.length = length
        self.width = width
    @abstractmethod
    def add_sides(self,x,y):
        pass
    @abstractmethod
    def square_sides(self,p):
        pass
class Rectangle(shape):
    def __init__(self, length, width):
        super().__init__(length, width)
    def add_sides(self, x, y):
        return x+y
    def square_sides(self, p):
        return p*p
    
    def Rect_perimeter(self):
        print("The perimeter of the rectangle is ",2*self.add_sides(self.length,self.width)," units")    
    
class Circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def add_sides(self, x, y):
        return x+y
    
    def square_sides(self, p):
        return p*p
    def Circle_perimeter(self):
        print("The area of a circle is ",3.14*self.square_sides(self.radius)," square units")
        
print()
        
rect_one = Rectangle(4,6)
circle_one = Circle(5)
rect_one.Rect_perimeter()
circle_one.Circle_perimeter()


#ASSIGNMENT THREE
#Create a receipt printing program with GUI interface 
#a more advanced detail more marks





        
        
        
        
             



