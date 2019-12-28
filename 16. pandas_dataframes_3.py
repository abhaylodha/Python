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
