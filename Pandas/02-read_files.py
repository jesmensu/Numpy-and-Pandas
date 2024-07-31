import pandas as pd

df = pd.read_csv('data.csv')
print(df)                   # only return the first 5 rows, and the last 5 rows
print(df.to_string())       # returns entire data
print(df.head())            # returns 5 first row
print(df.tail())            # return last 5 row

# Print information about the data
print(df.info())



df = pd.read_json('data.json')

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340
  }
}
df = pd.DataFrame(data)
print(df)