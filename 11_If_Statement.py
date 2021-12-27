# If Statement:

print(" ")
print("****** Exercise 1 ****** \n ")
#            Execute certain code when certain conditions are TRUE
#            and could execute other conditions are FALSE

is_male = False

if is_male:
    print("you are a male")
else:
    print("you are a female")

print(" ")  # is there to just to have space in output
print("****************** Comparison ************************************ \n ")
print("****** ( True & True ) ****** \n ")
is_male = True
is_tall = True

if is_male and is_tall:
    print("you are a tall male")
elif is_male and not (is_tall):
    print("you are short male")
elif not (is_male) and is_tall:
    print("you are a tall woman")
else:
    print("your not tall and not a male")


print(" ")
print("****** ( True & False) ****** \n ")
is_male = True
is_tall = False

if is_male and is_tall:
    print("you are a tall male")
elif is_male and not (is_tall):
    print("you are short male")
elif not (is_male) and is_tall:
    print("you are a tall woman")
else:
    print("your not tall and not a male")


print(" ")
print("****** (False & True) ****** \n ")
is_male = False
is_tall = True

if is_male and is_tall:
    print("you are a tall male")
elif is_male and not (is_tall):
    print("you are short male")
elif not (is_male) and is_tall:
    print("you are a tall woman")
else:
    print("your not tall and not a male")


print(" ")
print("****** (False & False) ****** \n ")
is_male = False
is_tall = False

if is_male and is_tall:
    print("you are a tall male")
elif is_male and not (is_tall):
    print("you are short male")
elif not (is_male) and is_tall:
    print("you are a tall woman")
else:
    print("your not tall and not a male")