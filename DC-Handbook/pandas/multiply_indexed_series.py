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

pop.index.names = ['state', 'year']
print(pop)


print('='*64)

print('California Poblacion 2010 =>', pop['California', 2010])
print(pop['California'])

print('='*64)

print('Poblacion por estados')
print(pop.loc['California': 'New York'])

print('='*64)

print('Poblacion 2010')
print(pop[:, 2010])

print('='*64)

print('Poblacion mayor a 22M')
print(pop[pop > 22000000])

print('='*64)

print(pop[['California', 'Texas']])

pop.to_csv('pop.csv', index=False)