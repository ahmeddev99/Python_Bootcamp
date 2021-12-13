# Building a Basic Calculator

print("********* number enter is going to pick as string and not as number *********")

num1 = input("Enter num: ")
num2 = input("Enter num2: ")

result = num1 + num2

print(result) # answer will give 4545 because the data enter is going to think as string, not as number


print("") # And better to write it because (int) needs you to enter whole number not decimal.
print("********* FLOAT *********")
num1 = input("Enter num: ")
num2 = input("Enter num2: ")

result = float(num1) + float(num2)

print(result)
