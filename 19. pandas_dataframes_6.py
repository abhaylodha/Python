import os
import pandas as pd

df = pd.read_csv(os.path.dirname(os.path.abspath(__file__)) + '\\census.csv')
print(df.head())

print("Distinct values from a column")
print(df['SUMLEV'].unique())
print(df)

print("After filtering data")
df = df[df['SUMLEV'] == 50]
#Same as below statement
#df = df.where(df['SUMLEV'] == 50).dropna()

print(df)

#Removing Unwanted Columns from DF
columns_to_keep = ['STNAME',
                   'CTYNAME',
                   'BIRTHS2010',
                   'BIRTHS2011',
                   'BIRTHS2012',
                   'BIRTHS2013',
                   'BIRTHS2014',
                   'BIRTHS2015',
                   'POPESTIMATE2010',
                   'POPESTIMATE2011',
                   'POPESTIMATE2012',
                   'POPESTIMATE2013',
                   'POPESTIMATE2014',
                   'POPESTIMATE2015']

df = df[columns_to_keep]
print("After removing unwanted columns")
print(df)

#Setting multilevel index.
df = df.set_index(['STNAME', 'CTYNAME'])
print("After setting multilevel index")
print(df)

#Querying Df with multilevel index.
#Returns a Series.
print(df.loc['Michigan', 'Washtenaw County'])

#Return Dataframe
print(df.loc[ [('Michigan', 'Washtenaw County')]])

#Return Dataframe
print(df.loc[ [('Michigan', 'Washtenaw County'),('Michigan', 'Wayne County')]])
