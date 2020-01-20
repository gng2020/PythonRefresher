#This is a comment. Below print hello world
"""
This is a whole chunk of comment
"""

print ("Hello World")

# set a string variable and an integer variable
str="Hello again !"
myInt=3
print (str, myInt)
print (str,myInt)

# And some weird way to assign same values to a few variable
x=y=z=10

print(x,y,z)

# Defining function (probably best to keep this on the top or another python file for best practice)
def myFunc():
    global w # global variable, rather than local to this definition.
    w="great great job!"
    return w

print (myFunc())
print (len(myFunc()))
print ((myFunc())[0:3]) # print first character up to 2th=3-1 character. A:B print A to B-1 index. NOT INCLUSIVE.
print (" abc d e f  ".strip()) # strip off white space at the beginning or end
print (myFunc().upper()) # upper
print (myFunc().lower()) # lower
print (myFunc().replace("e","eeeeeea")) # replace char



# type
print (type(w))
print (type(x))

a=1.0
print (type(a))
print (float(2)) # convert int to float
print (int(2.0)) # convert float to int
print (complex(2.0)+(1+2j)) # convert  to complex



a=True
print (type(a))

# List, sq bracket, separated by comma
x = [1,2.05, "banana"]
print (x)
#print (type(x))

# tuple, round bracket
y = (1,2.05, "banana")
#print (y)
#print (type(y))

# list is mutable but tuple is not
x[0]=10
# y[0]=2 (will be error)
x[1]="apple"
print (x) # for a list, can assign a diff data type to each entry

# And a dict, curly bracket with items separated by comma, but the pair separated by colon
z={"name":"jack", "age": 10}
print(z)
print (type(z))



#To access local Bash shell, first impo os
import os
print (os.getcwd())

#If and for
