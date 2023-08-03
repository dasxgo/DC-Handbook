import pandas as pd
import numpy as np

data = pd.Series([0.25, 0.5, 0.75, 1.0])
print(data)

print(data.values)
print(data.index)

print(data[1])

print(data[1:3])