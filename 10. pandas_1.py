import pandas as pd

#Series is an important data structure in Pandas which has Index integers and Index Labels
#It's cross of Lists and Dictionaries.
animals = ['Tiger', 'Bear', 'Moose' ]
p1 = pd.Series(animals)
print(p1)

numbers = [1,2,3,4,5]
p2 = pd.Series(numbers)
print(p2)

animals2 = ['Tiger', 'Bear', 'Moose', None ] # Data Type is set to None
p3 = pd.Series(animals2)
print(p3)

numbers2 = [1,2,3,4,5, None]  # None causes type conversion to float and adds NaN None
p4 = pd.Series(numbers2)
print(p4)

#Creating Series

sports = {'Archery': 'Bhutan',
          'Golf':'Scotland',
          'Sumo':'Japan',
          'Taekwondo' : 'South Korea'}

#Dictionary keys becomes indexes
s = pd.Series(sports)
print(s)
print(s.index)

# Indexes can be specified manually
s1 = pd.Series(['Tiger', 'Bear', 'Moose'],['India', 'America', 'Canada'])
print(s1)
print(s1.index)

sports2 = {'Archery': 'Bhutan',
          'Golf':'Scotland',
          'Sumo':'Japan',
          'Taekwondo' : 'South Korea'}

#Hockey is an extra Index for which no dictionary key exists.
#Golf is not present in indexes, so that is not preserved.
s2 = pd.Series(sports2, ['Archery', 'Sumo', 'Taekwondo', 'Hockey'])
print(s2)
print(s2.index)

print(s2.iloc[3])   #Prints 4th Index Value
#Same as above, but works when Series has index labels.
print(s2[3])   #Prints 4th Index Value

print(s2.loc['Sumo'])   #Prints Sumo Index Value
#Same as above, but works when Series has index labels.
print(s2['Sumo'])   #Prints Sumo Index Value

sports3 = pd.Series([110.0, 125.4, 73.5, 3., 67.97])
print(sports3)

print(sports3[0])
print(sports3.iloc[0])