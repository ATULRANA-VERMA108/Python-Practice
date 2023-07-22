#constructor: Constructor is invoked automatically when an object of a class is created.   
class Person:
 
  def __init__(self,name,occ):
   print("hey  I am a person ")
   self.name=name
   self.occ=occ

  def info(self):
    print(f"{self.name} is occupation {self.occ}")

a=Person("harry","developer")
b=Person("aria","dancer") 
a.info()   
b.info()
# print(a.name)
# a.name="divaya"
# a.occ="HR"
# a.info()


""" TYPES OF CONSTRUCTOR: TWO TYPS OF CONSTRUCTOR
 (1)parametrized constructor:When the constructor accepts arguments along with self, 
 it is known as parameterized constructor.
 (2)default constructor:When the constructor doesn't accept any arguments from 
 the object and has only one argument, self, in the constructor, 
 it is known as a Default constructor
                   """

# parametrized constructor :
class Details:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group

obj1 = Details("Crab", "Crustaceans")
print(obj1.animal, "belongs to the", obj1.group, "group.")

# default constructor:


class Details:
  def __init__(self):
    print("animal Crab belongs to Crustaceans group")
obj1=Details()