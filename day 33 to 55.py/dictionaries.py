# dictionaries: it is ordered collection of data items
info={'name':'atul','age':20,'eligible':True}
print(info)

# accessing single value by using key
print(info['name'])
print(info['age'])
print(info['eligible'])
print(info.get('name'))
print(info.get('age'))
print(info.get('eligible'))
#accessing multiple value by using values()
print(info.values())
# accessing keys
print(info.keys())
#accessing key-value pair
print(info.items())
#accessing key in the info.keys

for key in info.keys():
  print(f"The value corresponding to the key {key} is {info[key]}")
#accessing key,value in the info.items
for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}") 
  


