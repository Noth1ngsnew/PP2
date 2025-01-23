#Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

###########################################

#You can use the range() function to create an iterable:
newlist = [x for x in range(10)]

#################################

#Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]

##########################################

#Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]

###########################################

#Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]