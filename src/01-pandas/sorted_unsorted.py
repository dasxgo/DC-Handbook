import pandas as pd
import numpy as np

index = pd.MultiIndex.from_product([['a', 'c', 'b'], [1, 2]])
data = pd.Series(np.random.rand(6), index=index)
data.index.names = ['char', 'int']
print(data)

print('='*64)

data = data.sort_index()
print(data)

print('='*64)

print(data['a':'b'])


