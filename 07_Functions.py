#         Lists Functions

print("")  # is there to just to have space in output
print("****************** INDEX ************************************ \n ")

my_numbers = [4, 8, 15, 16, 23, 42]
#  index -->    0        1        2        3        4
friends = ["Shayaan", "Zayn", "Azaya", "Majda", "Rubal"]
# ["Shayaan", "Zayn", "Azaya", "Majda", "Rubal", 4, 8, 15, 16, 23, 42]
friends.extend(my_numbers) # adds my_numbers list to my friends and becomes as 1 list.
print(friends)


print(" ")  # is there to just to have space in output
print("****************** APPEND (adding more to the list) ****************** \n ")
# \n to print in next line
# ["Shayaan", "Zayn", "Azaya", "Majda", "Rubal", 4, 8, 15, 16, 23, 42]
friends.append("Jordan")
print(friends)


print(" ")  # is there to just to have space in output
print("****************** INSERT ************************************ \n ")
# ["Shayaan", "Zayn", "Azaya", "Majda", "Rubal", 4, 8, 15, 16, 23, 42]  <-- Lists
friends.insert(1, "Isam")
print(friends)


print(" ")  # is there to just to have space in output
print("****************** INDEX ************************************ \n ")
print(friends.index("Majda"))


print(" ")  # is there to just to have space in output
print("****************** Remove ************************************ \n ")
# ["Shayaan", "Zayn", "Azaya", "Majda", "Rubal", 4, 8, 15, 16, 23, 42]  <-- Lists
friends.remove("Rubal")
friends.remove(42)
print(friends)


print(" ")  # is there to just to have space in output
print("****************** POP ************************************ \n ")
# POP removes from the back side
# ["Shayaan", "Zayn", "Azaya", "Majda", "Rubal", 4, 8, 15, 16, 23, 42]  <-- Lists
friends.pop()
print(friends)


print(" ")  # is there to just to have space in output
print("****************** COUNT ************************************ \n ")
friends.count("Zayn")
print(friends)


print(" ")  # is there to just to have space in output
print("****************** SORT ************************************ \n ")
my_numbers.sort()
print(my_numbers)


print(" ")  # is there to just to have space in output
print("****************** CLEAR ************************************ \n ")
# ["Shayaan", "Zayn", "Azaya", "Majda", "Rubal", 4, 8, 15, 16, 23, 42]  <-- Lists
friends.clear()
print(friends)


