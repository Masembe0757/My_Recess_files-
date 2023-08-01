#Exception handling

Cars = ["Tesla","Virgo","Sienta","Mozida"]
try:
    print (Cars[2])
    print (Cars[9])
except:
    print("The item you want to access does do not exist")
finally:
    print("Execution done")
    
#An else statement can be added to a try to be executed after trying
    
    
#Raise exceptions
Weight = int(input("Enter your weight"))
if Weight < 0:
    raise Exception("Weight cant not be a negative value")
else:
    print("Your weight is ",Weight," kg")
    
#Custome exception
    
class WrongHeight (Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    
age = int(input("Enter your age"))
if age < 0 :
    raise WrongHeight("Height can not be a negative value")
else:
    print("Age saved successfully")
    
    
#Reading from a file

file_name = "data.txt"
file = open(file_name,"r")
contents =  file.read()
print(contents)


#Adding  data to a file ((a) appends end to end of existing text in the file
file = open(file_name,"a")
file.write(" and a good person")

#Writting to a file with (w) truncates the existing bytesize to zero and writes to a file
file = open(file_name,"w")
file.write("Iam Sendi Joseph")

#Other opening modes "a+","w+"
"""
Read = reads everything in a file
readline = reads first line of the file
readlines = reads multiple lines

"""
#Using with ensures file is closed automatically even whe an exception occurs
with open(file_name,"r") as file_to_read:
    print(file_to_read.readline()) # This will print the last line added by previous append operation


