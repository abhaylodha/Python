import numpy as np
import pandas as pd

original_sports_list = pd.Series({'Golf' : 'Scotland',
                                  'Archery':'Bhutan',
                                  'Sumo' : 'Japan',
                                  'Taekwondo' : 'South Korea'})

cricket_lovers_list = pd.Series(['Australia', 'India', 'England'], ['Cricket','Cricket','Cricket'])

print(original_sports_list)
print(cricket_lovers_list)

all_countries_sports_list = original_sports_list.append(cricket_lovers_list)

print(all_countries_sports_list)

#Adding a new Index and value pair to existing list.
all_countries_sports_list.loc['Hockey'] = 'India'
print(all_countries_sports_list.loc['Hockey'])
print(all_countries_sports_list)