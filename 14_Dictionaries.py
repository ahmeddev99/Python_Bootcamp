# Dictionaries:

monthConversions = {
    "Jan":  "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print (monthConversions["Nov"])

print (monthConversions["Mar"])

print (monthConversions.get("Dec"))

print (monthConversions.get("Dov")) # will giv you none

# - you can pass a default value instead on none.

print (monthConversions.get("Dov","Not a valid key"))

# - you can use numbers, strings in keys

