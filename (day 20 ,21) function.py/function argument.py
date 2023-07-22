# function will be four types in python 
# (1)default argument (2)keyword argument (3)variable length argument  (4)required arguments
# default argument: its provide default value when function argument is not provide the  value 
def average (a=9,b=2):
   print ("the average is ",(a+b)/2)
average(2,5)
# keyword argument :  we can provide the argument with value =key
average(b=9,a=2)
# requirment argument:we do not pass the argument value=key, In case use correct order 
def average (a,b,c=1):
  print ("the average is ", (a+b+c)/2)
  average(5,6)
#variable length : esme hum len() function use krte hai    

#keyword arbitrary argument:while creating a function ,then pass *a before the parameter name
def name (**name):
  print(type(name))
  print ("hello ",name["ram"],name["syam"],name["radhe"])

name(ram="god",syam="krishna",radhe="premika")