import pandas as pd

# Create a simple Pandas Series from a list
# Series is for one dimentional data
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar["y"])

# Series from dictionary
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)

# Dataframe =========================================

a = [[1, 7, 2],[2,8,9]]
df = pd.DataFrame(a, columns = ["Number1", "Number2", "Number3"])
# DataFrame is like a table with rows and columns and for 2D data
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)

# Locate Row
# Pandas use the loc attribute to return one or more specified row(s)
print(df.loc[0])
# calories    420
# duration     50

print(df.loc[[0]])
#    calories  duration
# 0       420        50

print(df.loc[[0, 1]])
#    calories  duration
# 0       420        50
# 1       380        40

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)
#           calories  duration
#   day1       420        50
#   day2       380        40
#   day3       390        45
print(df.loc["day2"])
print(df.loc["day2", "calories"])

data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
# del df["c"]
# df.pop("b")
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df)
print(df[2:4])

df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])
df = pd.concat([df,df2])             
print(df)
#    a  b
# 0  1  2
# 1  3  4
# 0  5  6
# 1  7  8

df = df.drop(0)     # If label is duplicated, then multiple rows will be dropped.
df.loc[:, ["a", "b"]]

print(df.iloc[0])         # 1 is the index or row number
print(df.iloc[3:5, 0:2])   # 3:5 is row index and 0:2 is the column number
# print(df.iloc[[1, 2], [0, 2]])
print(df.iloc[1:3, :])
print(df.iloc[1, 1])      # getting one value
print(df.iat[1, 1])

# Setting values by label:
# df.at[dates[0], "A"] = 0

# Setting values by position:
df.iat[0, 1] = 0



