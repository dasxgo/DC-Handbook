import pandas as pd
import numpy as np

data = pd.Series([0.25, 0.5, 0.75, 1.0],
                 index=['a', 'b', 'c', 'd'])

print(data)

data2 = pd.Series([0.25, 0.5, 0.75, 1.0],
                  index=['1', '2', '3', '4'])

print(data2)