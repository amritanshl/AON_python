def add(num1, num2): #parameter
    return num1+num2
def sub(num1, num2): #parameter
    print(num1-num2)
def mul(num1, num2): #parameter
    print(num1*num2)
def div(num1, num2): #parameter
    print(num1/num2)

add_l = lambda a ,b:a+b
sub_l = lambda a ,b:a-b
mul_l = lambda a ,b:a*b
div_l = lambda a ,b:a/b

print(add_l(55,11))

area_rec = lambda l,b,h: l*b*h
area_sphere = lambda r : (4/4)*3.14*(r**2)

check_num = lambda num : "Even" if num%2==0 else "Odd"

get_max = lambda a,b: a if a>b else b