import pandas as pd
import numpy as np

ind = pd.Index([2,3,5,7,11])
print(ind)

# Index as Inmutable Array

print(ind[1])

print(ind[::2])

print(ind.size, ind.shape, ind.ndim, ind.dtype)