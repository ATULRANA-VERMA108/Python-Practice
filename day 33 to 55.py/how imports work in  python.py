# to import a module in python ,you use th import statement  followed by the name of the module 

# import math
  
import math
result=math.floor(4.23)
result2=math.factorial(5)
print(result)
print(result2)

# from keyword : you can also  import specific function or variable from module using the from keyword

from math import sqrt,pi
result3=sqrt(7)*pi
print(result3)

""" importing everything :It's also possible to import all functions and variables from a module 
  using the * wildcard."""
from math import *

result = sqrt(9)
print(result)  # Output: 3.0

print(pi)  # Output: 3.141592653589793

# the " as " keyword : it is shortcut form the any function,module by the our assumption
import math as d
result4=d.sqrt(5)
print(result4)

""" the " dir" function: Finally, Python has a built-in function called dir
 that you can use to view the names of all the functions and variables defined in a module  """

import math
print(dir(math))


# from harry import welcome, harry
import harry as hr
import math

print(dir(math))
print(math.nan, type(math.nan))
hr.welcome()
print(hr.harry)