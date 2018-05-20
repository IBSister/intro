#This is a program full of the basics you might need to know 
#to work on the database repository
from pip._vendor.distlib.compat import raw_input

#Basics created on May 17th, 2018
#By: Christopher Wattananimitgul

#Setting up variables
string_variable = "Example"
integer_variable = 17
negint_variable = -5
floating_variable = 1786.04
complex_variable = 3.5j
a,b,c = 35,57,"Kemp"
#Longs are not used in this version

#Several variables, one value
d = e = f = 5 

#Delete the value 
del f

#Lists
list = [ "10", 11, 70.2] #Size can be changed

#Tuples
tuple = ("abc", 76, "yes", 2.23, "James", -33) #Size cannot be changed

#Dictionary (This one's confusing btw)
dict = { "name" : "john", "code" : 10, "game" : "no"}  #{Key:Value, Key:Value, Key:Value}

#Printing on PyDev
print(string_variable)
print(string_variable[0])
print(string_variable[2:5]) #Print Characters from 3 to 5
print(string_variable[2:]) #Prints everything from 3 to end

print(integer_variable)
print(integer_variable * 2)
print(integer_variable + negint_variable)

print(negint_variable)
print(floating_variable)
print(complex_variable)
print(a + b)
print(d + e)
#print(f) will just result in an error saying 'f' is not defined

#Everything you do with the String variable,
#you can do with the other variables

#if - else if - else statement
num = 100
num1 = 20
if(num == 100):
    print("Number is 100")
    #Nested if statement
    if(num < num1):
        print("Num1 is greater")
    else:
        print("Num is greater")
elif(num < 100):
    print("Number is less than 100")
else:
    print("Number is greater than 100")
    
#Loops!
count = 0
while(count < 5):
    print("Count is " , count) #To combine a string and int, use a comma
    count = count + 1
    
#Also works for lists and such
for letter in "Python":
    print("Current letter: " , letter)
    
#Functions
def concat(str1, str2):
    print(str1 + str2)
    
#Calling the function
concat("hi", "bye")

#Basic keyboard inputs
input1 = raw_input();
print("What you said:", input1)

#End May 19th, 2018
