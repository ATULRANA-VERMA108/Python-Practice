# else in loop 

# for i in []: #for the empty
for i in range(6):
  print(i)
else:
    print("sorry i is not present here ")
# using break in the  for loop
for i in range(6):
   print(i)
   if i==4:
    break
else:
    print("sorry i is not present here ")
# using break in while loop
i=0 
while i<7:
  i=i+1
  print(i)
  if i==4:
    break
else:
    print("sorry i is not present here ")

# given example: for the iteration 
for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")