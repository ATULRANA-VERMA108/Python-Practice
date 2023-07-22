""" Inheritance in python:     When a class derives from another class.
 The child class will inherit all the public and protected properties and
   methods from the parent class.In addition, it can have its own properties and methods,
   this is called as inheritance.  
   
   class BaseClass:
  Body of base class
class DerivedClass(BaseClass):
  Body of derived class
   
    types of inheritance : 
    (1)single inheritance
    (2)multiple inheritance
    (3)multilevel inheritance
    (4)hierarichal inheritance
    (5)hybrid inheritance

    """
  
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def showdetails(self):
        print(f"the name is Employee {self.id} is {self.name} ")
class programmer(Employee):
    def showLanguage(self):
        print("python is default language")

e1 = Employee("Rohan Das", 400)
e1.showdetails()
e2 = programmer("Harry", 4100)
e2.showdetails()
e2.showLanguage()



