import pandas as pd
import numpy as np

# hierarchical indices and columns

index = pd.MultiIndex.from_product([[2013, 2014], [1,2]], 
                                   names = ['year', 'visit'])
columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']],
                                     names = ['subject', 'type'])

# mock some data

data = np.round(np.random.rand(4,6), 1)
data[:, ::2] *= 10
data += 37

# Create the DataFrame

health_data = pd.DataFrame(data, index=index, columns=columns)
print(health_data)

print('='*64)

print(health_data['Guido'])

health_data.to_csv('healt_data.csv', index=False)



