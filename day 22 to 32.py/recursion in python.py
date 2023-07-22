# recursion in python ,which call itself
#find factorial using recursion 
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n* factorial (n-1)
print(factorial(4))
print (factorial(5))
#find fibonacci series
"""" f(0)=0, f(1) 
f(2)=f(0)+f(1) base case: if two number 0 and 1 then return 1 
general way for fibonacci :f(n)=f(n-1)+f(n-1): recursion case
"""
def fibonacci(n):
  # base case: the first two numbers in the series are 1
  if n == 1 or n == 2:
    return 1
  # recursive case: the next number is the sum of the previous two
  return fibonacci(n-1) + fibonacci(n-2)

# prompt the user for the number of terms to generate
num_terms = int(input("Enter the number of terms to generate: "))

# generate and print the Fibonacci series
for i in range(1, num_terms+1):
  print(fibonacci(i), end=" ")

    
   

