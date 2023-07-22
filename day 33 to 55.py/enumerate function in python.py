# enumerate function in python : its give  the value and index of each element 
marks=[21,12,23,99,32,1,4,5]
for index,mark in enumerate(marks):
    print(mark)
    if (index==3):
        print("excellance performance of atul verma")


# changing the start index:
for index,mark in enumerate(marks,start=1):
   print(index,mark)
   if(index==3):
       print("awesome atul")

# changing the start index:
# Loop over a list and print the index (starting at 1) and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)