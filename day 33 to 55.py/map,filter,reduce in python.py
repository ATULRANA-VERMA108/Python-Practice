""" MAP,FILTER AND  REDUCE FUNCTION :
 In Python, the map, filter, and reduce functions are built-in functions
 that allow you to apply a function to a sequence of elements and return a new sequence.
   These functions are known as higher-order functions,
 as they take other functions as arguments.        """

def cube(x):
    return x*x*x
print(cube(5))

l=[2,3,5,7]
# newl=[]
# for item in l:
    # newl.append(cube(item))

# map: build in function, (list,tuple,iterableobject)map(function, iterable)
# newl=list(map(cube,l)) 
newl=list(map(lambda x:x*x*x,l))   
print(newl)
#fiter:it is build in function, map(function, iterable)
#iterable: list,tuple and etc which perform basic operation
def filter_function(a):
    return a>4
newnewl=list(filter(filter_function,l))
print(newnewl)


# reduce: reduce(function, iterable):The function argument is a function that takes in two arguments
#  and returns a single value.

from functools import reduce 

# list of number
number=[1,2,3,4,5]

# sum of two number using the reduce function 
def mysum (x,y):
    return x+y
sum =reduce(mysum,number)
#print
print(sum)