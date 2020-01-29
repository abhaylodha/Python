import os
import pandas as pd

df = pd.read_csv(os.path.dirname(os.path.abspath(__file__)) + '\\log.csv')
df = df.set_index('time')
df = df.sort_index()
print(df)

print("Multi Level Index")
df = df.reset_index()
df = df.set_index(['time', 'user'])
df = df.sort_index()
print(df)
