import os
import pandas as pd

df = pd.read_csv(os.path.dirname(os.path.abspath(__file__)) + '\\olympics.csv', index_col = 0, skiprows = 1)
print(df.head())

print(df.columns)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold' + col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver' + col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze' + col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#' + col[1:]}, inplace=True) 

print("After renaming columns")

print(df.head())

df['Country'] = df.index
print("\nAfter adding country column")
print(df)
df = df.set_index('Gold')
print("\nAfter changing index to gold")

#Setting for displaying full dataframe columns.
with pd.option_context('display.max_rows', 5, 'display.max_columns', None):
    print(df)

#Get rid of the index
df = df.reset_index()
with pd.option_context('display.max_rows', 5, 'display.max_columns', None):
    print(df)
