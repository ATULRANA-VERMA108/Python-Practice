# indexing in tuple 
tup=(2,4,5,6,"ram",7,8,9,0,True)
print(type(tup),tup)
print(len(tup))
# postive indexing
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[5])
print(tup[9])
# negative indexing
print(tup[-4])
print(tup[len(tup)-4])
#check in item
if  4 in tup:
    print ("yes present in tuple ")
else:
    print ("not prsent in tuple ") 
#find tuple in range
print(tup[:5]) # take left range value is zero
print(tup[0:]) # at right range assume length of tuple by python complier
print(tup[4:-3])
print(tup[3:7])
# tuple is immutable  beacuse we are not change in tuple ,length of tuple ,at indexing value

#operation  in tuple 
""" tuple me operation ke liye  hum uski ek lit copy bnate hai to hum usko as a list treat krte hai then phir hum
usko tuple me convert kr dete hai"""
countries= ("india","bangladesh","russia","uk","usa ","chaina" )
temp=list(countries)
temp.append("barma")
temp.pop(4)
temp[2]="findland"
countries=tuple(temp)
print(countries)
#add two tuple
num=(4,5,6,7)
num2=(8,9,10)
num3=num+num2
print(num3)
# tuple method : build in method in tuple ,it is immutable (1)count():its find occurances
tuple2=(4,5,8,3,5,5,5)
res=tuple2.count(5)
print("occurance of 5 in tuple2 ",res)
#index method: its return the value first occurances that element in the given tuple"
# des=tuple2.index(5)
# print("occurance of 5 as index ",des)
des=tuple2.index(5,1,4)
print("indexing of multiple index",des)






