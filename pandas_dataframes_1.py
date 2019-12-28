import pandas as pd

purchase_1 = pd.Series ({'Name' : 'Chris',
                         'Item Purchased' : 'Dog Food',
                         'Cost' : 100.5})

purchase_2 = pd.Series ({'Name' : 'Kevyn',
                         'Item Purchased' : 'Kitty',
                         'Cost' : 130.2})

purchase_3 = pd.Series ({'Name' : 'Vinod',
                         'Item Purchased' : 'Bird Seed',
                         'Cost' : 59.7})

df = pd.DataFrame([purchase_1,purchase_2, purchase_3], index = ['Store 1','Store 2','Store 3'])

print("\nFull DF")
print(df)
print("\nDF Head")
print(df.head())
print("\nIndex - Store 1")
print(df.loc['Store 1'])

#chaining comes with a cost as loc/iloc/[] returns a copy of DF instead of view.
print("\nIndex - Store 1, Index - Name")
print(df.loc['Store 1'].loc['Name'])
print("\nIndex - Store 1, Index - Name")
print(df.loc['Store 1']['Name'])
print("\nIndex - Store 1, Index - Name")
print(df.loc['Store 1', 'Name'])

print('All items purchased')
print(df['Item Purchased'])

print('DF transpose')
print(df.transpose())
print()
print(df.T)

print("\nAll rows with Name and Cost columns")
print(df.loc[:, ['Name', 'Cost']])

df_copy = df.drop('Store 1')
print("\nDropping a Row")
print(df_copy)

df_copy = df.drop(axis=1, labels = 'Cost')  #Dropping column returns a new copy of DF
print("\nDropping a Column")
print(df_copy)

df_copy = df.copy()
del df_copy['Name']   #In place column deletion
print("\nDropping a Column")
print(df_copy)

df['Location'] = None
print("\nAdding a new Column")
print(df)

df['Location'] = 'Pune'
print("\nAdding a new Column")
print(df)

df.loc['Store 4'] = pd.Series ({'Name' : 'Abhay',
                         'Item Purchased' : 'Cattle Feed',
                         'Cost' : 350.5,
                         'Location' : 'Ashta'})

print("\nAdding a new Row")
print(df)
