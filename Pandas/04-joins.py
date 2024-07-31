import pandas as pd

df1 = pd.DataFrame({
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    }, index=[0, 1, 2, 3],)

df2 = pd.DataFrame({
        "A": ["A4", "A5", "A6", "A7"],
        "B": ["B4", "B5", "B6", "B7"],
        "C": ["C4", "C5", "C6", "C7"],
        "D": ["D4", "D5", "D6", "D7"],
    }, index=[0, 1, 2, 3],)

frames = [df1, df2]
result = pd.concat(frames)

df4 = pd.DataFrame( {
        "B": ["B2", "B3", "B6", "B7"],
        "D": ["D2", "D3", "D6", "D7"],
        "F": ["F2", "F3", "F6", "F7"],
    }, index=[2, 3, 6, 7], )

result = pd.concat([df1, df4], axis=1)
print(result)
result = pd.concat([df1, df4], axis=1, join="inner")    # join='inner' takes the intersection of the axis values
print(result)
result = pd.concat([df1, df4], axis=1).reindex(df1.index) # Takes index of df1
#     A   B   C   D    B    D    F
# 0  A0  B0  C0  D0  NaN  NaN  NaN
# 1  A1  B1  C1  D1  NaN  NaN  NaN
# 2  A2  B2  C2  D2   B2   D2   F2
# 3  A3  B3  C3  D3   B3   D3   F3

result = pd.concat([df1, df4], ignore_index=True, sort=False)
    #     A   B    C   D    F
    # 0   A0  B0   C0  D0  NaN
    # 1   A1  B1   C1  D1  NaN
    # 2   A2  B2   C2  D2  NaN
    # 3   A3  B3   C3  D3  NaN
    # 4  NaN  B2  NaN  D2   F2
    # 5  NaN  B3  NaN  D3   F3
    # 6  NaN  B6  NaN  D6   F6
    # 7  NaN  B7  NaN  D7   F7

s1 = pd.Series(["X0", "X1", "X2", "X3"], name="X")
result = pd.concat([df1, s1], axis=1)
#     A   B   C   D   X
# 0  A0  B0  C0  D0  X0
# 1  A1  B1  C1  D1  X1
# 2  A2  B2  C2  D2  X2
# 3  A3  B3  C3  D3  X3

s4 = pd.Series([0, 1, 2, 3])
s5 = pd.Series([0, 1, 4, 5])
d1 = pd.concat([s4, s5], axis=1)
d2 = pd.concat([s4, s5], axis=1, keys=["blue", "yellow"])

pieces = {"x": df1, "y": df2}
result = pd.concat(pieces)

# merge() performs join operations similar to relational databases like SQL.

left = pd.DataFrame({
        "key": ["K0", "K1", "K2", "K3"],
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
    })

right = pd.DataFrame({
        "key": ["K0", "K1", "K2", "K3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    })

result = pd.merge(left, right, on="key")

#   key   A   B   C   D
# 0  K0  A0  B0  C0  D0
# 1  K1  A1  B1  C1  D1
# 2  K2  A2  B2  C2  D2
# 3  K3  A3  B3  C3  D3

left = pd.DataFrame({
      "key1": ["K0", "K0", "K1", "K2"],
      "key2": ["K0", "K1", "K0", "K1"],
      "A": ["A0", "A1", "A2", "A3"],
      "B": ["B0", "B1", "B2", "B3"],
   })


right = pd.DataFrame({
      "key1": ["K0", "K1", "K1", "K2"],
      "key2": ["K0", "K0", "K0", "K0"],
      "C": ["C0", "C1", "C2", "C3"],
      "D": ["D0", "D1", "D2", "D3"],
   })
result = pd.merge(left, right, how="left", on=["key1", "key2"])
#   key1 key2   A   B    C    D
# 0   K0   K0  A0  B0   C0   D0
# 1   K0   K1  A1  B1  NaN  NaN
# 2   K1   K0  A2  B2   C1   D1
# 3   K1   K0  A2  B2   C2   D2
# 4   K2   K1  A3  B3  NaN  NaN

result = pd.merge(left, right, how="outer", on=["key1", "key2"])
result = pd.merge(left, right, how="outer", on=["key1", "key2"])
result = pd.merge(left, right, how="inner", on=["key1", "key2"])
result = pd.merge(left, right, how="cross")
result = pd.merge(left, right, on="key1", suffixes=("_l", "_r"))



# DataFrame.join() combines the columns of multiple, potentially differently-indexed DataFrame into a single result DataFrame.
result = left.join(right)
result = left.join(right, how="outer")
result = left.join(right, how="inner")
result = left.join(right, on="key")
result = left.join(right, on=["key1", "key2"], how="inner")

right2 = pd.DataFrame({"v": [7, 8, 9]}, index=["K1", "K1", "K2"])
result = left.join([right, right2])

