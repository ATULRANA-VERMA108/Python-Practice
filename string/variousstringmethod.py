str1="hello!!"
#rstrip() string method:remove any trailing character 
print(str1.rstrip("!"))
str2="silver spoon"
#replace() string :replace any word with another
print(str2.replace("sp","m"))
#split() string :ye list me use kiya jata hai
print(str2.split(" "))
#capatalize() string:ye sentence ki first letter ko captial me change kr deta hai
str3="the landlord is very miser"
print(str3.capitalize())
#count:return the no of times the given value has occurred within the given string 
str4="AbacoiFkaIlaIlabdce"
countstr=str4.count("a")
print (countstr)
# endwith:check the string ends with a given value like as yes then return true ,else return false 
print(str4. endswith("e"))
#find() method:search for the first occurrance of the given value
print(str3.find("is"))
#index() method: searches for the first occurrance of the given value and the returns the index
print(str3.index("l"))
#isalnum the sting ,it is makes by the A-Z,a-z,0-9 then returns true otherwise return falssalnum():chee
str5=" raju talwar"
print(str5.isalnum())
#isalpha() string method:
print(str5.isalpha())
#islower:if string in the lowercase then return the value true otherwise return false 
print(str5.islower())
#is pritable(): returns true if all the value within the given string are printable 
print (str5.isprintable())
#isspace():return true only and only if the string contains white spaces ,otherwise return false
str6=" "
print (str6.isspace())
#istittle():first letter of each word of the string is capatallized then return the true 
#isupper(): agar string uppercase  me hoga to string true return karegi nhi to false 
#starswith():check the starts string with a given value if yes then return true otherwise return false
#swapcase():in the swapcase ,uppercase change to lowercase and lowercase change to the uppercase 
#tittle ():captalized each letter in the given string



