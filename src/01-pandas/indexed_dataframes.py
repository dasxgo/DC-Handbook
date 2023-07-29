import pandas as pd
import numpy as np

index = pd.MultiIndex.from_product([[2013, 2014], [1,2]], 
                                   names = ['year', 'visit'])
columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']],
                                     names = ['subject', 'type'])


data = np.round(np.random.rand(4,6), 1)
data[:, ::2] *= 10
data += 37


health_data = pd.DataFrame(data, index=index, columns=columns)
print(health_data)

print('='*64)

print(health_data['Guido', 'HR'])

print('='*64)

print(health_data.iloc[:2, :2])

print('='*64)

print(health_data.loc[:, ('Bob', 'HR')])

print('='*64)

idx = pd.IndexSlice
print(health_data.loc[idx[:, 1], idx[:,'HR']])



