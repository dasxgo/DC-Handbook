import pandas as pd
import numpy as np

def make_df(cols, ind):
    data = {c: [str(c) + str(i) for i in ind]
            for c in cols}
    return pd.DataFrame(data, ind)

print(make_df('ABC', range(3)))

print('='*64)

x = [1,2,3]
y = [4,5,6]
z = [7,8,9]

print(np.concatenate([x, y, z]))

print('='*64)

x1 = [[1,2], 
      [3,4]]

print(np.concatenate([x1, x1], axis = 1))

print('='*64)

# Concatenation with pd.concat


ser1 = pd.Series(['A', 'B', 'C'], index=[1,2,3])
ser2 = pd.Series(['D', 'E', 'F'], index=[4,5,6])


print(pd.concat([ser1, ser2]))

print('='*64)


