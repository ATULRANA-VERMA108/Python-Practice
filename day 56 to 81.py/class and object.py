# creating a class 

class Person:
    name= "rohan"
    occupation="software enginner"
    networth=10
    def info(self):
        print(f"{self.name} is a occupation {self.occupation} and networth is {self.networth}")
"""  self parameter:
The self parameter is a reference to the current instance of the class,
 and is used to access variables 
that belongs to the class. """



# creating the object:
a=Person()
b=Person()
c=Person()

a.name="rang bahadur"
a.occupation="teaching"
a.networth=30

b.name="aria"
b.occupation="kpop dancer"
b.networth=4500000000
 
c.name="atul"
c.occupation="surgen"
c.networth=700000000000 
# print(a.name,a.occupation,a.networth)
a.info()
b.info()
c.info()

# self parameter :
class Details:
    name = "Rohan"
    age = 20

    def desc(self):
        print("My name is", self.name, "and I'm", self.age, "years old.")

obj1 = Details()
obj1.desc()