#FUNCTION
""" group  of statements that perform a specific times."""
"""2 type of function: built-in and user defined"""
"""print(),len(),type(),range():- built in functions"""
""""""
""" def func_name(parameter1,parameter2,parameter3,......)"""   # function definition
""" func_name(arg1,arg2,arg3,.....)"""  #argument
""" parameter and argument not compulsory."""
#sum of 2 number multiple times
a=2
b=3
sum=a+b
print(sum)
a=4
b=5
sum=a+b
print(sum)
a=1
b=7
sum=a+b
print(sum)

"""instead"""
def sum(a,b):       #definition
    return a+b
print(sum(2,3))     #argument
print(sum(4,5))
print(sum(1,7))

def ph():
    print("hello")

ph()
ph()

#avg of 3 no.s
def avg(a,b,c):
    return((a+b+c)/3)
print(avg(3,5,7))

def prod(a,b):
    return a*b
print(prod(4,"d"))
print(prod(2,3))

# default value
def prod(a,b=4):
    return a*b
print(prod("a"))
print(prod(2,3))
print(prod(6))

