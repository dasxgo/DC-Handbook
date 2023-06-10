import pandas as pd
import numpy as np

# Series as Dictionary

data = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index = ['a', 'b', 'c', 'd'])
print(data)

print(data['b'])

print('a' in data) 

print('respuesta =>', 'a' in data)

print('='*64)

print(data.keys())

print('='*64)

print(list(data.items()))

print('='*64)

data['e'] = 1.25
print(data)


