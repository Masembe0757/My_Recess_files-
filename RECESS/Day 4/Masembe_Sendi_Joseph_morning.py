#A class is a blue print of objects
#An object is an instance of a class
#A class has attributes
#Example one
class Car:
    def __init__(self,brand,make,name) :
        self.brand = brand
        self.make = make
        self.name = name
    def car_start(self):
        print("The car has started")
    def car_stop(self):
        print("The car has stopped")
car_one = Car("Benz","2050","Mercedes Benz")
car_one.car_start()
car_one.car_stop()
print("The name is ",car_one.name)  
print()
print() 

#Example two
#named attributes
class Emp:
    def __init__(self,name,salary,post) :
        self.name = name 
        self.salary = salary
        self.post = post
    def Employee_details(self):
        print("The name is ",self.name)
        print("The salary is ",self.salary)
        print("The post is ",self.post)
emp_one = Emp(post="kikoni",salary=50000000,name="Sendi Joseph")
emp_one.Employee_details()  
print()
print()  

#Example three
#Bank system
class Bank :
    def __init__(self,balance,acc_name) :
        self.acc_name = acc_name
        self.balance = balance
        
    def Deposit(self,value):
        self.balance +=value
        self.Show()
        print("Thank you for depositing")
    def Withdraw(self,value):
        if(value<=self.balance):
            self.balance-=value
        else:
            print("Insufficient balance!")
        self.Show()
        print("Thank you for withdrawing")
    def Show(self):
        print("The account name is ", self.acc_name)
        print("The balance on account is ",self.balance)
        
cust_one = Bank(500000,"Sendi Joseph")
cust_one.Deposit(100000)
cust_one.Withdraw(6000)

print()
print()

#Calculating Bonus for employee
#calculate and display employee bonus of salary(emp1 :150,000,emp2: 230,000)
class Bonus:
    
    def __init__(self,name,salary) :
        self.name = name
        self.salary = salary
    def calc_bonus(self,value):
        self.salary*=value
        print("The bonus of ",self.name," is ",self.salary)
emp1 = Bonus("employee1",150000)
emp1.calc_bonus(0.15)
emp2 = Bonus("employee2",230000)
emp2.calc_bonus(0.15)



#ASSIGNMENT ONE



#Encapsulation
#Exercise converte temp(37) in celsious to Fahrengeit
class Temp :
    def __init__(self,temp):
        self._temp = temp
        self.to_fahrenheit(self._temp)
        
    def to_fahrenheit(self,cel):
        print("The temperature in celcius is ",cel)
        cel = ( cel *(9/5) )+ 32
        fah = cel
        print("The tempertaure in fahrenheit is ",fah)
        

temp_one = Temp(37)


#ASSIGNMENT TWO


#Show encapsulation with employee information to 
# give a pay increament(Saalry with employee informtaion to a new_salary) 
# e.g from 7800 to 1000000


#In my illuastration I will increase salary using a rate of the employee's salary 
class Employee :
    def __init__(self,name,wage,age) -> None:
        self._name = name
        self._wage = wage
        self._age  = age
    def  Icreament_salary(self,rate):
        extra = self._wage *rate
        print(self._name,"'s current salary is ",self._wage,"shillings and has an age of ",self._age,"years")
        print(self._name,"'s bonus is ",extra, "shillings")
        print(self._name,"'s new salary is ", self._wage+extra,"shillings")
employee_one = Employee("Godwin Geoffrey",2000000,50)
employee_one.Icreament_salary(0.05)

print()







#Personal practice

#Inheritance
class Person :
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def Eat(self):
        print("A person can eat")
class Student(Person): #A student is a person hence a student inherits non private attributes an methods of base class Person
    def Details(self):
        print("Student name is ", self.name," and age is ",self.age)
st_one = Student("Sendi Joseph",19) #Child accessing attributes of parent
st_one.Eat() #Child accessing method of parent
st_one.Details()

#Polymorphism
#Ability of a sigle object or method to have multiple forms

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
animal_one = WildAnimal("Deer")
animal_two = Animal("Tiger")
animal_two.Run()
animal_one.Run()

        
        
