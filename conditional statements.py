# CONDITIONAL STATEMENTS

# IF-ELIF-ELSE
name = input("Name:")
age = int(input("Age:"))
if (age >= 18):
    print(name,"is eligible to vote!")
else:
    print(name,"is not eligible to vote!")

# Traffic light code
light = input("Colour of Traffic light:")
if (light == "red"):
    print("Stop")
elif (light == "green"):
    print("Go")
elif (light == "yello"):
    print("Wait")
else:
    print("Light is broken")

# Single Line IF (Ternary Operator)
food = input("food:")
eat = "yes" if food == "cake" or food == "coke" else "no"
print (eat)
#alternative
print("yes") if food == "cake" or food== "coke" else print("no")

# Clever IF (Ternary Operator)
vote = ("no","yes") [age >= 18]
print(vote)

# Nesting
if (age >= 18):
    if (age >= 80):
        print ("you cannot drive")
    else:
        print("you can drive")
else:
    print("you cannot drive")
