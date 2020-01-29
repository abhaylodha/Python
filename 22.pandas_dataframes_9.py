
import os
import pandas as pd

r1 = pd.Series({'name' : 'Chandler Bing',
                'activity' : 'party',
                'timestamp' : '2017-08-04 08:00:00'})

r2 = pd.Series({'name' : 'Harry Kane',
                'activity' : 'football',
                'timestamp' : '2017-08-04 13:00:00'})

r6 = pd.Series({'name' : 'Harry Kane',
                'activity' : 'party',
                'timestamp' : '2017-08-04 13:15:00'})

r3 = pd.Series({'name' : 'John Doe',
                'activity' : 'beach',
                'timestamp' : '2017-08-04 14:00:00'})

r4 = pd.Series({'name' : 'Joey Tribbiani',
                'activity' : 'party',
                'timestamp' : '2017-08-04 10:00:00'})

r7 = pd.Series({'name' : 'Joey Tribbiani',
                'activity' : 'party',
                'timestamp' : '2017-08-04 16:00:00'})

r8 = pd.Series({'name' : 'Joey Tribbiani',
                'activity' : 'football',
                'timestamp' : '2017-08-04 16:00:00'})

r5 = pd.Series({'name' : 'Monica Geller',
                'activity' : 'travel',
                'timestamp' : '2017-08-04 07:00:00'})

df = pd.DataFrame([r1, r2, r3, r4, r5, r6, r7, r8])
df['timestamp'] = pd.to_datetime(df['timestamp'], infer_datetime_format=True)

print(df)

print (df.name)
print (df.name.str)
print (df.name.str.split(" ", expand=True))

#df['name'] = df.name.str.split(" ", expand=True)

print("After name split")
print(df)

df1 = df.groupby('name')['activity'].value_counts()

print("After Group by")
print(df1)

df2 = df.groupby('name')['activity'].value_counts().unstack()
print("After Group by and unstack")
print(df2)

df3 = df2.fillna(0)
print("After Group by and unstack and fillna")
print(df3)

print("Group by and timestamp difference with previous value")
df4 = df.sort_values(by=['name','timestamp'])
df4['time_diff'] = df.groupby('name')['timestamp'].diff()
print(df4)

print("timestamp difference with previous value")
df5 = df.sort_values(by=['name','timestamp'])
df5['time_diff'] = df5['timestamp'].diff()
print(df5[df5.groupby('name')['timestamp'].cumcount() > 0])
print(df5)