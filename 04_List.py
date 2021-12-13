# Lists:

print("")
print("********* String, Numbers, Boolean *********")


friends = ["Shayaan", "Zayn", "Azaya", 5, 10, 1, True]
# the types of data that exist here inside is String ^^
# you can store a numbers and booleans as well

print(friends[1])
print(friends[4])
print(friends[1:])


print("")
print("********* Index *********")


#  index -->    0        1        2        3        4
friends1 = ["Shayaan", "Zayn", "Azaya", "Majda", "Rubal"]
# ^^ this is actually variable, and this is the list,
#        this is or you can consider it a list of variable

# these are the indexes, so Shayaan is going to
#  take the index zero, zayn index one, azaya index 2


print(friends1[1])
print(friends1[-1])
print(friends1[1:])
print(friends1[1:3])


print("")
print("********* MODIFY *********")

friends2 = ["Shayaan", "Zayn", "Azaya", "Majda", "Rubal"]

friends1[4] = "Baba"  # Replace index name to modify value inside of python list
print(friends2[1:])
print(friends2[4])
