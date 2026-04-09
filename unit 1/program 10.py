add = lambda a,b: a + b
sub = lambda a,b: a - b
mul = lambda a,b: a * b
div = lambda a,b: a / b if b != 0 else "Error division by zero"

num1 = float(input("enter the first number:"))
num2 = float(input("enter the second number:"))
op = input("enter operator (+, -, *, /):")

if op == '+':
    print("result:", add(num1 , num2))
elif op == '-':
    print("result:", sub(num1 , num2))
elif op == '*':
    print("result:", mul(num1 , num2))
elif op == '/':
    print("result:", div(num1 , num2))
else:
    print("invalid operator")
