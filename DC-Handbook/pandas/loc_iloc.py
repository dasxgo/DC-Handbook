import pandas as pd
import numpy as np

data = pd.Series(['a','b','c'], index=[1,2,3])
print(data)

# explicit index when indexing

print(data[1])

# Implicit index when slicing

print(data[1:3])

print('='*64)

# loc

print(data.loc[1])
print(data.loc[1:3])

print('='*64)

# iloc

print(data.iloc[1])
print(data.iloc[1:3])






