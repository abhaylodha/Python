import pandas as pd

purchase_1 = pd.Series ({'Name' : 'Chris',
                         'Item Purchased' : 'Dog Food',
                         'Cost' : 22.5})

purchase_2 = pd.Series ({'Name' : 'Kevyn',
                         'Item Purchased' : 'Kitty Litter',
                         'Cost' : 2.5})

purchase_3 = pd.Series ({'Name' : 'Vinod',
                         'Item Purchased' : 'Bird Seed',
                         'Cost' : 5.0})

df = pd.DataFrame([purchase_1,purchase_2, purchase_3], 
                  index = ['Store 1','Store 1','Store 2'])

df['Location']=df.index

print(df)
df = df.set_index(['Location','Name'])

print(df)


df.loc[('Store 2', 'Kevyn'), :] = pd.Series ({'Item Purchased' : 'Kitty Food',
                                'Cost' : 3.00})

print(df)
