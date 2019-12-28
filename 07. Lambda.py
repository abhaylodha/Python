people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 
          'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

#option 1
for person in people:
    print(split_title_and_name(person) == 
          (lambda person:person.split(" ")[0] + " " + person.split(" ")[-1] )(person))

#option 2
for person in people:
    print(split_title_and_name(person) == 
          (lambda x : split_title_and_name(x))(person))

#option 3
print(list(map(split_title_and_name, people)) == list(map(split_title_and_name, people)))
