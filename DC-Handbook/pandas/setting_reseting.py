import pandas as pd
import numpy as np

import pandas as pd
import numpy as np

index = [('California', 2010), ('California', 2020),
         ('New York', 2010), ('New York', 2020), 
         ('Texas', 2010), ('Texas', 2020)]

populations = [37253956, 39538223, 19378102, 20201249, 25145561, 29145505]

pop = pd.Series(populations, index=index)

index = pd.MultiIndex.from_tuples(index)

pop = pop.reindex(index)
print(pop)

print('='*64)

pop_flat = pop.reset_index(name='population')
print(pop_flat)

print('='*64)

pop_flat.columns = ['state', 'year', 'population']
print(pop_flat)

print('='*64)

print(pop_flat.set_index(['state', 'year']))
