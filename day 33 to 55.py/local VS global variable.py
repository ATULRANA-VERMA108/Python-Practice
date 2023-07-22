# local varibale : it is access in the locally in the function 
# global variable: it is access in the global ,its mean every where we access in the code editor
# some following examples , we are discussing the local and global variable

x=4
print(x)

def hello():
   x=5
   print(f"local value of x is {x}")
   print("hare krishna")

print(f"global value of x is {x}")
hello()
x=5

print(f"global value of x is {x}")


# following access local variable and global variable :

def my_function():
  y = 5 # local variable
  print(y)

my_function()
print(x)
# print(y)  
""" this will cause an error because y is a local variable and is not 
accessible outside of the function"""