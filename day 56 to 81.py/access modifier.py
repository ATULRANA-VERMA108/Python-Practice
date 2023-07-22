"""   access specifier/modifier:
Access specifiers or access modifiers in python programming are used to limit 
the access of class variables and class methods outside of class while implementing 
the concepts of inheritance.                                                    

types of access modifier:
(1)public access modifier
(2) private access modifier
(3) protected access modifier

"""

"""(1)public access specifier:All the variables and methods (member functions)
 in python are by default public. Any instance variable in a class followed by
   the 'self' keyword ie. self.var_name are public accessed.  """

class Student:
    # constructor is defined
    def __init__(self, age, name):
        self.age = age               # public variable
        self.name = name             # public variable

obj = Student(21,"Harry")
print(obj.age)
print(obj.name)



"""private access : isme hum direct access nhi kr sakte hai lekin indirectly access krte hai
  esme hum (__double uderscore ) use krte hai  ."""

class Employee:
    def __init__(self):
        self.__name="ramramji"

a=Employee()
# print(a.__name) # cannot be accessed by directly .

print(a._Employee__name)#can access indirectly.(ese hum name mangling ke nam se bhi jante hai)

# print(a.__dir__()) #ye eski attribute ko show krta hai 

"""  private access modifier method class Student: """


"""   protected access modifier:In object-oriented programming (OOP), 
the term "protected" is used to describe a member
 (i.e., a method or attribute)     using single (_)  
  ye conventional method hai """

class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())









