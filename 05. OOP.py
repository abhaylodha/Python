class Person :
    department = "Center of Excellence"

    def __init__(self, name="default_name", location = "default_Location"):
        self.name = name
        self.location = location

    def set_name (self, new_name) :
        self.name = new_name

    def set_location(self,new_location) :
        self.location = new_location

    def get_location(self) :
        return self.location

print(Person.department)

p = Person(location = "location", name = "name")
p1 = Person(name = "name")
p2 = Person(location = "location")
#p.set_location("Pune")
#p.set_name("ABC")

print(p)
print(p.name)
print(p.get_location())

print(p1.name)
print(p1.get_location())

print(p2.name)
print(p2.get_location())
