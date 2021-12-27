# Building a Better Calculator:

num1 = float(input("Enter first number: "))
op = input("Enter Operation: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)


else:
    print("Invalid 4Operator")
