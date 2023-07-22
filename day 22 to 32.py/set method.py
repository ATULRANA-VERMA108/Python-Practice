# set method: set operation in python: (1)union and update: take union two set ,then using update 
# (2)intersection and update : take intersection two set,then update the set 
s1={2,3,4,5,6}
s2={7,8,2}
"""union and update : at union we take all value of both sets in union but in update 
we form in union form then access eachset"""
(s1).update(s2)
print(s1)
print(s1.union(s2))
"""intersection and update_:take common value of both set then take  in update value take 
 common value each set """
print(s1.intersection(s2))
(s1).intersection_update(s2)
print(s2)
#symmetric differance: vo sari value jo common me nhi  aati hai
print((s1).symmetric_difference(s2))
#union of sets
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3)
#update of union of sets
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.update(cities2)
print(cities)
# intersection of sets
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)
#update of intersection of sets
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
print(cities)
# symmetric differance : vo sari value jo common me exit nhi krta hai
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)
# symmetric_ differance_update: esme symmetic diffrance store hoti hai after opration 
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities) 
#diffrance of set : jo phle set me ho lekin dusre set me na ho
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)
#diffrance_update: esme update store hota hai diffrance ka
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
print(cities.difference(cities2))
"""set method : build in set method :(1)is disjoint : ye check krta hai dono set ko ki element
 agar common nhi hota hai to wo true return krta hai agar common hota hai to false return krta hai 
 (2)is superset(): esme hum check krte hai ki sabhi set orginal set  me present hai agar present hota
 hai to True return krte hai otherwise false return krte hai
 (3)is subset():esme hum  check krte hai ki given set orginal set ka part hai ki nhi 
 (4)add(): by this method we are adding the new item in the set
 (5)update(): update the value  according to between set value comes in orginal set 
 (6)remove(): ye value ko remove krta hai but esme error raise hota hai 
 (7)pop (): ye random value ko bahar nikalta hai lekin hum access value ko krke bhi hum bahar nikal skte hai
(8 )del(): ye delete krta hai set ko aur name error deta hai 
(9)clear(): ye set ke sabhi value ko clear krta hai aur empty set ko print kr deta hai 
(10)check in item in set: ye item ko check krta hai by the accessing of for loop
"""

#is disjoint()

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))

#is superset()

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))

#is subset()

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))

# add()

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)

#update()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)

#remove()

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)

#discord ()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.discard("Seoul")
print(cities)

#pop()

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

#del()

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
print(cities)

#clear()

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)

#check if item exits
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")