"""lambda function: a lambda function is a small anonymous function without a name. 
It is defined using the lambda keyword"""

# def double(x):
    # return x*2
# print(double(5))
def appl(fx, value):
  return 6 + fx(value)

double =lambda x:x*2
cube=lambda x:x*x*x
avg=lambda a,b,c:(a+b+c)/3
print(double(6))
print(cube(4))
print(avg(5,5,8))
print(appl(lambda x: x * x , 2))

# Function to calculate the product of two numbers
def multiply(x, y):
    return x * y

# Lambda function to calculate the product of two numbers
lambda x, y: x * y

# Lambda function to calculate the product of two numbers,
# with additional print statement
lambda x, y: print(f'{x} * {y} = {x * y}')
