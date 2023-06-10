import pandas as pd
import numpy as np

indA = pd.Index([1,3,5,7,9])
indB = pd.Index([2,3,5,7,11])

print(indA.intersection(indB))

print(indA.union(indB))

print(indA.symmetric_difference(indB))

