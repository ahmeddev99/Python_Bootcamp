# working with Strings




phase = "AZAYA LOVES SMILING"
phase1 = "azaya loves to kiss"

print("********* UPPER *********")
print(phase.upper())
print(phase1.upper())

print("********* LOWER *********")
print(phase.lower())
print(phase1.lower())

print("********* ISUPPER *********")
print(phase.isupper())
print(phase1.isupper())

print("********* ISLOWER *********")
print(phase.islower())
print(phase1.islower())

print("********* UPPER & ISUPPER *********")
print(phase.upper().isupper())
print(phase1.upper().isupper())

print("********* LOWER & ISLOWER *********")
print(phase.lower().islower())
print(phase1.lower().islower())

print("********* INDEX *********")
print(phase[4])
print(phase1[6])

print("********* How to find INDEX # *********")
print(phase.index("L"))
print(phase1.index("k"))
print(phase.index("SMI"))
print(phase1.index("loves"))


print("********* REPLACE *********")
print(phase.replace("SMILING", "HUGS"))

