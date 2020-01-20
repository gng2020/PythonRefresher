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

age = 12
name="Jack"
txt = "My name is {}, and I am {} " # placeholder
print(txt.format(name,age))

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

x.append("melon")
x.insert(2,"orange")
x.insert(4,"pineapple")
x.insert(4,"appricot")


print (x) # for a list, can assign a diff data type to each entry
x.remove("melon")
print (x)
print (x[-1])
print (x[2:5])
print (len(x))

# a set
s={"a","b","c","a"}
s.add("e")
s.remove("b")   # or discard
print (s) # set ignores repeated item
l2=["k","l"]
s2={"x","y","z"}
s.update(l2)
print(s)
s.update(s2)
print(s)

# And a dict, curly bracket with items separated by comma, but the pair separated by colon
z={"name":"jack", "age": 10}
print(z)
print (type(z))

print (z.get("name"))
z["name"]="john"
z["heigh"]=180
print (z)

#If elif else, :. and or.
favFood = ["carrot", "banana"]
if "apple" in favFood:
    print("Yes, apple is my favorite food!")
else:
    print("No, apple is NOT my favorite food!")

a=5
if a==6:
    print ("a==6")
elif a==5:
    print ("a==5")
else:
    print ("no idea !")


#To access local Bash shell, first impo os
import os
print (os.getcwd())

