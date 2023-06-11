import pandas as pd
import numpy as np

index = [('California', 2010), ('California', 2020),
         ('New York', 2010), ('New York', 2020), 
         ('Texas', 2010), ('Texas', 2020)]

populations = [37253956, 39538223, 19378102, 20201249, 25145561, 29145505]

pop = pd.Series(populations, index=index)
print(pop)

index = pd.MultiIndex.from_tuples(index)

pop = pop.reindex(index)
print(pop)

print(pop.unstack(level=0))

print(pop.unstack(level=1))

print(pop.unstack().stack())