import pandas as pd
import numpy as np

population_dict = {'California': 39538223, 'Texas': 29145505, 'Florida': 21538187, 'New York': 2021249, 'Pennsylvania': 13002700} 

population = pd.Series(population_dict)

print(population)

print(population['California'])
print(population['California' : 'Florida'])
