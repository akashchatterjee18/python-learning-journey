# SETS
"""
collection of unordered items
each element in the set must be unique & immutable
set is mutable but elements must be immutable
avoids multiple entry
cant store list/dict in sets as they are mutable
"""

sets={1,2,2,2,3,3,1,4,4,"hello","world"}
print(sets)
print(type(sets))
print(len(sets))

set1 = {}
set2 = set()
print(set1)
print(set2)
print(type(set1))   #emp dict
print(type(set2))   #emp set

# Functions
sets.add("war") # adds a new value
print(sets)
sets.remove(4)  # removes provided value
print(sets)
sets.pop()      # removes a random value
print(sets)
sets.clear()    # empties the set
print(sets)
set1 = {1,2,3,4}
set2 = {2,3,4,5}
print(set1.union(set2))         #union
print(set1.intersection(set2))  #intersection

# set comprehension is same as dictionary comprehension