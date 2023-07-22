# raising custom error : it use for handling error in the syntax,code
a=int(input("enter any value between 5 and 9 :"))

if(a<5 or a>9):
    raise ValueError("value of should be between 5 and 9")