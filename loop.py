# LOOP (while,for)

# WHILE LOOP

"""WAP to print "hello" 100 times"""
i=1
while i<=100:
    print("hello")
    i+=1

"""WAP to print 1 to 100"""
i=1
while i<=100:
    print(i)
    i+=1

"""WAP to print 100 to 1"""
i=100
while i>=1:
    print(i)
    i-=1

"""WAP to print the table of 23"""
i = 1
while i <=10:
    c = 23 * i
    print(c)
    i+=1

"""WAP to print the following list using while loop:
        [1,4,9,16,25,36,49,64,81,100]"""
n = [1,4,9,16,25,36,49,64,81,100]
i=0
while i < len(n):
    print(n[i])
    i+=1

""" Search for a number 81 in this tuple using while loop
    (1,4,9,16,25,36,49,64,81,100)"""
m = (1,4,9,16,25,36,49,64,81,100)
i=0
while i < len(m):
    if m[i] == 81:
        print ("found at index",i)
    i = i+ 1

# Break and Continue
""" break : ends the loop
    continue : terminates the execution in the current iteration
& continues with the next iteration"""

""" Search for a number 81 in this tuple using loop and break
    (1,4,9,16,25,36,49,64,81,100)"""
m = (1,4,9,16,25,36,49,64,81,100)
i=0
while i < len(m):
    if m[i] == 81:
        print ("found at index",i)
        break
    else:
        print("finding...")
    i = i+ 1

""" Print each element of the group except 36 and 64 from the tuple
    (1,4,9,16,25,36,49,64,81,100)"""
i=0
while i < len(m):
    if m[i]==36 or  m[i]==64:
        i+=1
        continue
    print(m[i])
    i+=1

""" Make a list of odd and even number square number seperateky from the tuple
    (1,4,9,16,25,36,49,64,81,100)"""
i=0
j=0
e = []
o = []
while i < len(m) and j < len(m):
    if m[i] % 2 == 1:
        o.append(m[i])
        i += 1
        continue
    e.append(m[i])
    i += 1

    if m[j] % 2 != 1:
        e.append(m[j])
        j += 1
        continue
print("the list of even square numbers :",e)
print("the list of odd square numbers :",o)



# FOR LOOP
num = [1,2,3,4,5,6,7,8,9,10]
for i in num:
    print(i)
#
nu = (1,2,3,4,5,6,7,8,9,10)
for j in nu:
    print(j)

#
name="Akash Chatterjee"
for char in name:
    print(char)
print("end")

#
for c in name:
    print (c)
else:
    print("end")

# search t in name
for t in name:
    if t=="t":
        print("t found")
    else:
        print("no t found")
else:
    print("end")


# search t in name using break
for t in name:
    if t=="t":
        print("t found")
        break
else:
    print("end")
"""execute only if false statement fails"""

"""WAP to print the following list using for loop:
        [1,4,9,16,25,36,49,64,81,100]"""
for i in n:
    print(i)


"""Search for the number 81 appearing the 1st time in this tuple using for loop
    (1,4,9,16,25,36,49,64,81,100)"""
q=(1,4,9,16,25,36,49,64,81,100,81)
p=0
for i in q:
    if i == 81:
        print("81 found at index", p)
    p+=1

"""Search for a number 81 in this tuple using for loop
    (1,4,9,16,25,36,49,64,81,100)"""
q=(1,4,9,16,25,36,49,64,81,100,81)
p=0
for i in q:
    if i == 81:
        print("81 found at index", p)
        break
    p+=1


# RANGE
"""
range(start,stop,step value)
for i in range (5) will give results from 0 to 4
for i in range (1,5) will give results from 1 to 4
for i in range (1,5,2) will give reuslts for 1,3
"""

for i in range (5):
    print(i)
for i in range (1,5):
    print(i)
for i in range (2,101,2):
    print(i)
for i in range (1,101,2):
    print(i)
for i in range (1,101):
    print(i)
for i in range (100,0,-1):
    print(i)
for i in range(1,11):
    print(3*i)

# PASS Statement (no work,just null loop) ( also can be used in if else statements)
age = int(input("age"))
if age >= 18:
    pass
else:
    print("you're a minor")

# WAP to print the sum of 1st 100 natural numbers
sum=0
for i in range(1,101):
    sum=sum+i
print(sum)

# WAP to print the factorial of 100
f=1
for i in range(1,101):
    f*=i
print(f)