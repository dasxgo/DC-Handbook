import pandas as pd
import numpy as np

index = [('California', 2010), ('California', 2020),
         ('New York', 2010), ('New York', 2020), 
         ('Texas', 2010), ('Texas', 2020)]

populations = [37253956, 39538223, 19378102, 20201249, 25145561, 29145505]

pop = pd.Series(populations, index = index)

index = pd.MultiIndex.from_tuples(index)

pop = pop.reindex(index)
print(pop)

print(pop[:, 2020])

print('-'*64)

# Extra Dimension

pop_df = pop.unstack()
print(pop_df)

print('-'*64)

print(pop_df.stack())

print('-'*64)

pop_df = pd.DataFrame({'total': pop, 
                        'under18': [9284094, 889892, 
                                    4318033, 4181528, 
                                    6879014, 7432474]})
print(pop_df) 

print('-'*64)

f_u18 = pop_df['under18'] / pop_df['total']
print(f_u18.unstack())





