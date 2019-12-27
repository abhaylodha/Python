numbers = []

for n in range(0,10) :
    if n % 2 == 0 :
        numbers.append(n)

print(numbers)

numbers1 = (n for n in range(0,10) if n % 2 == 0)
print(numbers1)  # Does not print anything. It just creates a Generator object.
print(list(numbers1)) #Converts Generator object into a list.

numbers2 = [n for n in range(0,10) if n % 2 == 0] #Creates a list directly.
print(numbers2)


#### Convert function into a list comprehension

def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst

print(times_tables() == [i*j for i in range(10) for j in range (10)])

print(times_tables())
print([i*j for i in range(10) for j in range (10)])

#### Finding possible user Ids. User Id has two letters and two numebrs.
lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

answer = [i+j+k+l for i in lowercase for j in lowercase for k in digits for l in digits ]
print(answer)
