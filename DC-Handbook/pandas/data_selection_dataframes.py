import pandas as pd
import numpy as np

# DataFrame as Dictionary

area = pd.Series({'California': 423967, 'Texas': 695662, 'Florida': 170312, 'New York': 141297, 'Pennsylvania': 119280})
pop = pd.Series({'California': 3958223, 'Texas': 29145505, 'Florida': 21538187, 'New York': 20201249, 'Pennsylvania': 13002700})

data = pd.DataFrame({'area': area, 'pop': pop})
print(data)



print(data['area'])

print('='*64)

print(data.area)

print('='*64)

print(data.pop is data['pop'])

print('='*64)

data['density'] = data['pop'] / data['area']
print(data)


print('='*64)

# DataFrame as two dimensional array

print(data.values)

print('='*64)

print(data.T)

print('='*64)

print(data.values[0])

print('='*64)

print(data['area'])

print('='*64)


print(data.iloc[:3,:2])

print('='*64)

print(data.loc[:'Florida', :'pop'])

print('='*64)

print(data.loc[data.density > 120, ['pop', 'density']])

print('='*64)

data.iloc[0,2] = 90
print(data)

print('='*64)

# Aditional indexing Coventions

print(data['Florida':'New York'])


print('='*64)

print(data[1:3])

print('='*64)

print(data[data.density>120])











