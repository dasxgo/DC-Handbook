import pandas as pd
import numpy as np

data = pd.Series([1, np.nan, 'hello', None])
print(data.isnull())

print('='*64)

print(data[data.notnull()])

print('='*64)

# Droping Null values

print(data.dropna())

print('='*64)

df = pd.DataFrame([[1, np.nan, 2], [2, 3 , 5], [np.nan, 4, 6]])
print(df)

print('='*64)

print(df.dropna())

print('='*64)

print(df.dropna(axis='columns'))

print('='*64)

df[3] = np.nan
print(df)

print('='*64)

print(df.dropna(axis='columns', how='all'))

print('='*64)

# Dropna rows

print(df.dropna(axis='rows', thresh=3))



