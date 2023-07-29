import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(4,2), 
                  index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2,]],
                  columns=['data1', 'data2'])

print(df)

print('='*64)

data = {('California',2010): 37253956,
        ('California', 2020) : 39538223, 
        ('New York', 2010) : 19378102, 
        ('New York', 2020): 20201249, 
        ('Texas', 2010): 25145561,
        ('Texas', 2020) : 29145505}

print(pd.Series(data))
