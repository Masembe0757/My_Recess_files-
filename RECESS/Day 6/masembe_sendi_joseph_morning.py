#Regular expressions
"""
\d > matches digit
\w > matches alphabeticall character
\s > matches whitespace character
[^ ] > matches character not with in thhe square brackets
[] > matches character with in square brackets
$ > matches th end of a line
^ > Matches the start of a a line
? > matches zero or one occurance of the proceeedong character or group
+ > matches one or one occurance of the proceeedong character or group


Matching and searching
regex re.match(), re.search. re.findal()

#Example one Demonstrating regex | Match First Word, Match Group, Match all Numbers
    """
    
import re
text = "Hello, Iam Sendi Joseph. Iam a programmer with 500 years  of experience"

match1 = re.search(r"\b\d+\b",text)
if match1:
    print("Digit matches found : ",match1.group())
    print()
match2 = re.findall("\b\b",text)
if match2:
    print("found : ",match2.group())
    
#Email validation
def validate_mail(email):
    pattern = r"^[\w\.\-]+@[\w\.-]+\.\w+$"
    if re.match(pattern,email):
        return True
    else:
        return False
    
print(validate_mail("sendigmail.com"))
print(validate_mail("sendi@gmail.com"))

#Generators and iterators
# "yield" generator
# Iterator '__iter__' or'__next__'

def factorial(num):
    if num == 0:
        return 1 #yield 1
    elif num == 1:
        return 1
    else:
        return num * factorial(num-1) #yield
    
print(factorial(3))
print()


#next
def square(n):
    yield n**2
for i in range(2,6):
    print("The square of ",i," is ", next(square(i)))
    
    
#Decorator @my_decorator
#Decorators allow to modify the behaviour of functions or without classes
#