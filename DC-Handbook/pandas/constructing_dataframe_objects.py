import pandas as pd
import numpy as np

area_dict = {'California': 423967, 'Texas': 695662, 'Florida': 170312, 'New York': 141297, "Pennsylvania": 110280}
population_dict = {'California': 39538223, 'Texas': 29145505, 'Florida': 21538187, 'New York': 2021249, 'Pennsylvania': 13002700}


population = pd.Series(population_dict)
area = pd.Series(area_dict)
states = pd.DataFrame({'population': population, 'area': area})


df_population = pd.DataFrame(population, columns=['population'])
print(df_population)

print('='*64)

# from list to dicts

data = [{'a' : i, 'b': 2*i}
        for i in range(3)]

print(pd.DataFrame(data))

print('='*64)

# from a dictionary of series object

print(pd.DataFrame({'popularion': population, 'area': area}))




