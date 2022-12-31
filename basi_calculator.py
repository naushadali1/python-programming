def sum(a,b) :
    add=a+b
    print(add)

def sub(a,b) : 
    diff=a-b
    print(diff)

def mul(a,b) : 
    product=a*b
    print(product)

def  div(a,b) : 
    dived =a/b
    print(float(dived))

num1 =int(input('Enter First Number :'))
num2 =int(input('Enter Second Number :'))
parameter =(input('Enter Parameter \(+,-,*,/) :'))

if parameter == '+':
    sum(num1,num2)
elif parameter == '-':
    sub(num1,num2)
elif parameter == '*' :
    mul(num1 ,num2)
elif parameter == '/' :
    (div(num1,num2) )
else :
    print("Invalid Parameter")
