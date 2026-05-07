age = int(input("Enter the age: "))
if age<=5:
    print("This is an infant ")
elif age> 5 and age <18:
    print("This is a teenager ")
elif age >=18 and age <60:
    print("This is an adult ")
else: 
    print("retired person")
