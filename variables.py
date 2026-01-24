# Topic - Variables

# Typing next line
a = "I AM AKASH CHATTERJEE.\nMY AGE IS 18. \nGOODBYE"
print(a)
# Assigning value
name = "Akash" + " " + "Chatterjee"
print(len(name), name[7], name[1:7])
""" 'len' gives number of character in the string. counts spaces as well. str[] provides index value.
str[starting_index:ending_index] implies the slicing, i.e.' provides from starting index to the previous index of ending index.
The ending index is not inluded in slicing!'
"""
age = 18
old = False
a = None

# Printing value
print("My name is:", name)
print("My age is:", age)

# Printing Datatypes
print(type(name))
print(type(age))
print(type(old))
print(type(a))

# Print Sum and Difference of 2 no.s
a = 2
b = 5
sum = a + b
print(sum)
diff = a - b
print(diff)

# Operators
c = "@"
print(a*b*c)
a , b = "2" , 5
print((a+c)*b)
d = 1.2
e = -1.2
f = -4
g = d / f
h = d // f
i = d % f
j = e / f
k = e // f
l = e % f
m = f ** b
print(g,h,i,j,k,l,m)

# COMMENTING
# single line comment
""" multiple
line
comment"""

# Input in Python
name = input("Name:")
age = int(input("Age:"))
print("My name is:", name)
print("My age is:", age)
print("My name is:", name,"and I am", age,"yrs old.")

