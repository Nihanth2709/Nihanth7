# calculator with operators
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
op = input("enter +,-,/,*: ")
if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    print("Result:", num1 / num2)
else:
    print("Invalid operator")