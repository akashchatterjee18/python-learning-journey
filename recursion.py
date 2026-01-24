# RECURSION
"""
loops and recursion are interrelated.
anything which can be done using loop can be done using recursion and vice versa.
"""

def show(n):
    print(n)
show(5)
show(4)
show(3)
show(2)
show(1)
"""
now i want to print
5
4
3
2
1
using show function only once (recursion)
"""
#recursive function
m=int(input("enter a number:"))
def show(n):
    if n==0:            # base case
        return
    print(n)
    show(n-1)
    print("end")
#show(5)
show(m)
#show(2*m)

# factorial
def factorial(n):
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)
print(factorial(m))


# will be revised again during DSA
