#LIST

fruit = ["banana", "apple", "litchi","guava"]
eg = ["a","p","p","l","e"]
marks = [94.4, 95.2, 99.2,66.7, 45.2]
print(marks)
print(type(marks))  # print type of the dataset marks variable store
print(len(marks))   # print the length of the list


# INDEXING in LIST
print(marks[0])   # print the value stored in 0th index
print(marks[3])   # print the value stored in 3rd index

"""
Strings are immutable. can't be changed
Lists are mutable. can be changed
"""
word = "hello"
print(word[0])
# word[0] = y  invalid. new values can't be assigned in a string
marks[0] = 87.3
print(marks)

# Slicing
print(marks[1:4])   # from 1st index to 3rd index
print(marks[:4])    # from 0th index to 3rd index
print(marks[1:])    # from 1st index to last index
print(marks[-3:-1]) # from -3rd index to -2nd index backward (99.2,66.7)

# Functions in List
marks.append(88.8)  # adds new value at the end
marks.reverse()     # reverses the list
print(marks)
a = marks.sort()        # sorts in ascending order. Returns NONE as it changes the string itself
print(marks,a)
b = marks.sort(reverse = True)    # sorts in descending order. Returns NONE
print(marks,b)
fruit.sort()        # alphabetical order in ascending order
print(fruit)
fruit.insert(2,"mango") # inserts new value at preffered position
print(fruit)
eg.remove("p")  # removes the first occurence of an element, here "p"
print(eg)
fruit.pop(4)    # remove the element of the given index
print(fruit)

# WRITE A PROGRAM TO ASK THE USER TO ENTER NAMES OF THEIR 3 FAVOURITE MOVIES & STORE THEM IN A LIST
movies=[]
movies.append(input("enter 1st movie:"))
movies.append(input("enter 2nd movie:"))
movies.append(input("enter 3rd movie:"))
print(movies)

# WAP TO CHECK IF A LIST CONTAINS A PALINDROME OF ELEMENTS.
if marks.copy == marks.reverse:
    print("palindrome")
else:
    print("not a palindrome")




#list comprehension
new_marks = [x-2 for x in marks]
print(new_marks)

cubes = []
for x in range(11):
    if x % 2 == 0:
        cubes.append(x**3)
print("using for loop cube of even number till 10:",cubes)


cube = []
cubex = [x**3 for x in range(0,11,2)]
# or cubex = [x**3 for x in range(11) if x % 2 == 0]
print("using list comprehension of even number till 10:",cubex)
