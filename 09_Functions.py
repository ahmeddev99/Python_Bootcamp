# Functions -->  - A collection of codes that performs aspecific task

# - Number of codes that perform one thing put them together
            #    and call them at any time.


def say_hi():
    print("Hello User")
say_hi()

def say_bye():
    print("Good Day")
say_bye()


print(" ") #  Endentation is there
           # --> It wont be excuted automatically until you call it sayhi() to call it

print("****************** TOP & BOTTOM ************************************ \n ")

print("Top")
say_hi()
say_bye()
print("Bottom")


print(" ")  # is there to just to have space in output
print("****************** PARAMETERS ************************************ \n ")
# PARAMETERS --> piece of information you cannot call the function without giving it the parameters.

def say_python(name, age, school):
    print("Love Python " + name + "How old are you " + age + "What school you go to " + school)
say_python("Zayn ", "5 ", "Pre-K ")


print(" ")  # is there to just to have space in output
print("****************** PARAMETERS WITH STRING ************************************ \n ")

def say_python(name, age):
    print("Hello " + name + " you are " + str(age))
say_python("Walid", 50)


print(" ")

def say_python(name, age, school):
    print(name + "Love Python "  "and is " + str(age) + " old " "goes to " + school)
say_python("Zayn ", 5, "Pre-K ")
say_python("Shan ", 10, "School 5 ")
say_python("Zayn ", 1, "momma & baba ")

# --->  - Break the code up into function that will be more effecient.