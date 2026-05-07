# import funcs 
# from funcs import add, sub, mul, div
from funcs import add as a, sub as s, mul as m, div as d, add_l


num1 = int(input("enter first number: "))
num2 = int(input("enter second number: ") )
choice = input("Enter the choice: ")





if choice == "/":
    if num2 != 0:
        myval = d(num1,num2)
        print(myval)
        
    else:
        print("Error: cannot divide it by zero")
elif choice =="*":
    m(num1,num2)
elif choice =="+":
    a(num1,num2)
elif choice =="-":
    s(num1,num2)
else:
    print("Error: Invalide Operator, Please choose from /, *, + and -")



