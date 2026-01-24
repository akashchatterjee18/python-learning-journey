# Tuples
marks = (45,49,45,76,87,49,45,86,98)
# immutable(can't be changed)
print(marks)
print(type(marks))
print(marks[4],marks[2])

# marks[3] = 67 not allowed. can't add or assign a new value.
num=()
print(num)  #empty tuple
print(type(num))

# indexing and slicing are same in tuple as strings and list

# Functions in Tuple
print(marks.index(49))  # returns the 1st appearance of the element
print(marks.count(45))  # returns the count of the element
