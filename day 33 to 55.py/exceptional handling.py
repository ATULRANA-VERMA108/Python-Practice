# exception handling concept 
# try...except block using

a=int(input("enter the number : "))
print(f"multiplication table of {a} is :")
try:
    for i in range(1,11):
        print(f"{int(a)}*{i}={int(a)*i}")
except:
    print("invalid input  ")
    print("some line important code line")
    print("end of the program ") 

    #  try ...except....except :
# try:
    # num = int(input("Enter an integer: "))
# except ValueError:
    # print("Number entered is not an integer.")       