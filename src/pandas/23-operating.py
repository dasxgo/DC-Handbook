import pandas as pd
import numpy as np

rng = np.random.default_rng(42)
ser = pd.Series(rng.integers(0, 10, 4))
print(ser)


df = pd.DataFrame(rng.integers(0, 10, (3,4)), 
                  columns=['A','B', 'C', 'D'])
print(df)

print(np.exp(ser))

print(np.sin(df*np.pi/4))

print('='*64)

# Index Alignment

# Index Aligment in Series

area = pd.Series({'Alaska': 1723337, 'Texas': 695662, 'California': 423967}, name = 'area')
population = pd.Series({'California' : 3958223, 'Texas' : 29145505, 'Florida' : 21538187}, name = 'population')

print(population/area)

print(area.index.union(population.index))

print('='*64)


A = pd.Series([2,4,6], index = [0,1,2])
B = pd.Series([1,3,5], index = [1,2,3])

print(A+B)

print('='*64)

print(A.add(B, fill_value=0))

print('='*64)

# Index Alignment in DataFrames

A = pd.DataFrame(rng.integers(0, 20, (2 , 2)), columns=['a', 'b'])
print(A)


B = pd.DataFrame(rng.integers(0, 10, (3, 3)), columns=['b', 'a', 'c'])
print(B)


print(A+B)

print('='*64)

print(A.add(B, fill_value=A.values.mean()))


print('='*64)

# Operations Between DataFrames and Series

A2 = rng.integers(10, size=(3,4))
print(A2)

print(A2 - A2[0])

print('='*64)

df = pd.DataFrame(A2, columns=['Q', 'R', 'S', 'T'])
print(df - df.iloc[0])

print('='*64)

print(df.subtract(df['R'], axis=0))

print('='*64)

halfrow = df.iloc[0, ::2]
print(halfrow)

print(df - halfrow)