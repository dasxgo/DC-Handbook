import pandas as pd
import numpy as np

print(pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b',], [1, 2, 1, 2]]))

print('='*64)

print(pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1), ('b', 2)]))

print('='*64)

print(pd.MultiIndex(levels=[['a', 'b'], [1,2]],
                    codes=[[0,0,1,1], [0,1,0,1]]))
