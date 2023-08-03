import pandas as pd
import numpy as np

data = pd.Series([1, np.nan, 2, None, 3], index = list('abcde'), dtype='Int32')
print(data)

df = pd.DataFrame([[1, np.nan, 2], [2, 3, 5], [np.nan, 4, 6]])


# fillna me remplaza los valores con cero

print(data.fillna(0))

print('='*64)

# Forward fill
 
print(data.fillna(method='ffill'))

print('='*64)

# back fill
print(data.fillna(method='bfill'))

print(df)

df[3] = np.nan
print(df)

print('='*64)

print(df.fillna(method='ffill', axis=1))

