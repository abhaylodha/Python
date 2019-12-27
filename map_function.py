
store1_prices = [10.0, 23.0, 75.0, 45.0, 34.0]
store2_prices = [14.0, 22.0, 72.0, 48.0, 38.0]

cheapest = map(min, store1_prices, store2_prices)

print(store1_prices)
print(store2_prices)
print(cheapest)   # Does not print anything as iti lazy evaluation.

#Below itertion actually evalautes the map function.
#It's very efficient in Big Data for memory management.
for p in cheapest :
    print (p)
    
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    values = person.split(" ")
    return values[0] + " " + values[2]

print("List of people")
print(people)

titles_and_last_name = map(split_title_and_name, people)

print(titles_and_last_name)  #Prints only references

print(list(titles_and_last_name)) #Iterates and evaluates map function to create a list object.

print("Using for loop")
for p in titles_and_last_name :   #Iterable has nothing left. So print nothing here.
    print(p)

