
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

#This is boolean masking. Will set to True where condition Gold > 0 is met, else False.
#It will create either 1 Dimensional Series or a DataFrame.
t = df['Gold'] > 0

print(type(t))
print(t)

#overlay the boolean mask on original dataframe
print("Only Gold")
only_gold = df.where(t)
print(only_gold)

print(only_gold['Gold'].count())

only_gold = only_gold.dropna()
print("After dropping na")
print(only_gold)

t = (df['Gold'] > 0) | (df['Gold.1'] > 0)
gold = df.where(t).dropna()
print(gold)
