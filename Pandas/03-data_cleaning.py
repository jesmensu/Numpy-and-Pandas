import pandas as pd

# Cleaning Empty Cells  ===============================================
df = pd.read_csv('data.csv')

# drop row with empty cells.
new_df = df.dropna()    #  Create new dataframe
df.dropna(inplace = True)   # drops rows in original dataframe

# Replace Empty Values
df.fillna(130, inplace = True)
df["Calories"].fillna(130, inplace = True)   # Replace NULL values in the "Calories" columns

x = df["Calories"].mean()
x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace = True)     # Replace with the mean, mediun or mode of the column

# Cleaning Data of Wrong Format =========================================
# Convert Into a Correct Format
df['Date'] = pd.to_datetime(df['Date'])   # empty date in row converts to a NaT (Not a Time) which can remove before convert with dropna

# delete the row with value x
df.drop(x, inplace = True)


# Removing Duplicates ===================================================
# To discover duplicates, we can use the duplicated() method
# The duplicated() method returns a Boolean values for each row
print(df.duplicated())
df.drop_duplicates(inplace = True)      # Remove duplicates 


