# DICTIONARY
""" used to store data values in key:value pair.
unordered, mutable & dont allow duplicate keys.
"""
"""
keys can be of any datatype.
"""
info = {
    "name" : "Akash",
    "age" : 18,
    "learning" : "python",
    "subjects" : ["maths","physics","chemistry"]
}
print(info)
print(type(info))

print(info["name"],info["age"])

# Reassigning a value to a key
info["name"] = "Akash Chatterjee"
info["score"] = 98
print(info)

# Nested Dict
stu = {
    "name":"Akash",
    "surname":"Chatterjee",
    "score":{
        "Math":98,
        "Physics":97,
        "Chemistry":96
        }
    }
print(stu)

# Functions
print(stu.keys())   # returns all keys in form of list
print(stu.values()) # returns all values in form of list
print(stu.items())  # returns all itrm(key,value) in form of tuple
print(stu.get("name"))  # returns the value acc to the provided key
name = {"name":"jabonaa",}
stu.update(name) # update an item to the dict
print(stu)
name = {"name":"Akash",}
stu.update(name)
print(stu)

""" we can interchange the datatype as well"""
print(list(stu.keys()))
print(tuple(stu.values()))
print(len(list(stu.items())))


#dictionary comprehension
numex = {1,2,3,4,5}
print(numex)
numexx = {x**2 for x in numex}
print(numexx)