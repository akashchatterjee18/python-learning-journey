# Pandas

import numpy as np
import pandas as pd

#* Creating a series
"""
Inside an array multiple datatypes are not stored.
But in series we can store multiple datatypes
"""
labels = ['a','b','c']
my_list = [10,20,30]
arr = np.array([40,50,60])
dictionary = {1 : 100,2 : 200,3 : 300}
print(pd.Series(labels))
print(pd.Series(my_list))
print(pd.Series(arr))
print(pd.Series(my_list,index = labels)) # we call the index points as labels only
print(pd.Series(arr,index = labels))     # and the data is called data points
print(pd.Series(dictionary))



#* Dataframes : combination of multiple series together

# Creation of Dataframes
datadict = {
    'Name' : ['Joyjeet','Akash','Rishab','Ayush'],
    'Age' : [18,24,19,32],
    'City' : ['New Delhi','Kolkata','Mumbai','Bengaluru'],
    'Salary' : [5000,1500,9000,2000]
}
df1 = pd.DataFrame(datadict)
print(df1)

datalist = [
    ['Joyjeet',18,'New Delhi',5000],
    ['Akash',24,'Kolkata',1500],
    ['Rishab',19,'Mumbai',9000],
    ['Ayush',32,'Bengaluru',2000]
]
df2 = pd.DataFrame(datalist)
colm = ['Name','Age','City','Salary']
print(df2)
df3 = pd.DataFrame(datalist,columns = colm)
print(df3)
print(df3['Name'])
print(df3[['Name','City']])

# Creating a new colm
df3['Designation'] = ['Economist','Engineer','Doctor','Businessman']
print(df3)

# Removing a colm both temporarily and permanently
print(df3.drop('Designation',axis = 1))     # Will remove it for the current execution only
print(df3)  # Designation will be shown here
print(df3.drop('Designation',axis = 1,inplace = True)) # Removes completely
print(df3)

# Removing a row
print(df3.drop(3,axis = 0)) # inplace = True works here as well

"""
axis = 0 horizontal drop
axis = 1 vertical drop
"""

# Showing a particular row or element
print("\"")
print(df2.loc[0])
print(df3.loc[0])
print(df3.loc[0,"Salary"])

# Selecting subsets of rows and colums
print(df3.loc[[0,1],["Name","City","Salary"]])
print(df3.loc[[2,3],["Name","City"]])

""" only those people whose age is more than 20 """
print(df3[df3["Age"] > 20])
print(df3[(df3["Age"] > 20) & (df3["Salary"] > 1800)])


#* Missing Data

# Finding missing data
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, 5],
    'C': [1, 2, 3, np.nan, np.nan],
    'D': [1, np.nan, np.nan, np.nan, 5]
}
df4 = pd.DataFrame(data)
print(df4)
print(df4.isna())
print(df4.isna().sum())
print(df4.isna().any())

# Removing missing data
df5 = df4.dropna()  # removes all row with even atleast 1 null value
print(df5)
df6 = df4.dropna(thresh = 3)    # removes the rows with less than threshold null values
print(df6)

# Filling missing data
df7 = df4.fillna(0) # replace all the null values with 0
print(df7)

values = {'A': 100,'B':200,'C':300,'D':400}
df8 = df4.fillna(value = values)
print(df8)

df9 = df4.fillna(df4.mean())
print(df9)


#* Merging, Joining and Concatenation of 2 dataframes

# Merging of 2 DataFrames
employees = pd.DataFrame({              # dataframe 1
    'employee_id': [1, 2, 3, 4, 5, 6],
    'name': ['Virat', 'Rohit', 'Peter', 'Dhoni', 'ABD', 'Ishan'],
    'department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Sales']
})
salaries = pd.DataFrame({               # dataframe 2
    'employee_id': [1, 2, 3, 6, 7],
    'salary': [60000, 80000, 65000, 70000, 90000],
    'bonus': [5000, 10000, 7000, 8000, 12000]
})
print(employees)
print(salaries)

a = pd.merge(employees,salaries)
print(a)
b = pd.merge(employees,salaries, on= 'employee_id')
print(b)
"""
a and b have same value.
on= is used to merge the dataframe based on the common column.
Since there is only one common column so on= is not required
"""
c = pd.merge(employees,salaries, on= 'employee_id', how='inner')
print(c)
d = pd.merge(employees,salaries, on= 'employee_id', how='outer')
print(d)
e = pd.merge(employees,salaries, on= 'employee_id',how= 'left')
print(e)
f = pd.merge(employees,salaries, on= 'employee_id',how='right')
print(f)
"""
how= inner is by default even if i dont add that at the end.
thus a,b and c have same outputs.
inner means merges using the common values of the common rows.
outer means merges all the values of common column and leave the value 'NaN' wherever ther is no value.
left means merges the left value of the two dataframe provided.
right means merges the right value of the two dataframe provided.
"""

