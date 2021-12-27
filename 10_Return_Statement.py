# Return Statement (((Part 2 of Functions )))

print(" ")  # is there to just to have space in output
print("****************** exercise 1 ************************************ \n ")

def cube(num):
    return num * num + num
result = cube(5)
print(result)


print(" ")  # is there to just to have space in output
print("****************** exercise 2 ************************************ \n ")

def cube(num):

    return num*num*num

print(cube(3))

print(" ")  # is there to just to have space in output
print("****************** exercise 3 ************************************ \n ")

def cube(num):

    return num*num*num

result = cube(4)

print(result)


print(" ")  # is there to just to have space in output
print("****************** exercise 4 ************************************ \n ")

# --> you can't put code after return because return is breaks out of the function.


def cube(num):
    print("test") # it will print everything before RETURN
    return num*num*num

    print("test") # it wont print anything after RETURN

result = cube(4)

print(result)



print(" ")  # is there to just to have space in output
print("****************** exercise 5 ************************************ \n ")


# #  it wont work

#         def cube(num):

#         num*num*num

#         cube(3)

#         print(cube(3))


