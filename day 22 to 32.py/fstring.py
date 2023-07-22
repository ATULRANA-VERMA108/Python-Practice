# string formating in python : using format method
letter="hey my name is {0} and i am from {1}"
country="india"
name="atul"
print(letter.format(name,country))
#fstring method: it is easy way for the combine the new string in previous string
print(f"hey my name is {name} and i am from {country}")
print(f"{2*30}")
# double curly bracket fstring ke ander likhe stament ko waise hi hubhu print kr dega 
print(f"hey my name is {{name}} and i am from {{country}}")
