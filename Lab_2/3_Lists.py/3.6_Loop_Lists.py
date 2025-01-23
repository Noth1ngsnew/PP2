# A for loop that iterates through all items in a list:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

#########################################

# A for loop using index numbers to access list items:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

#########################################

# A while loop that iterates through the list until all items are printed:
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1

#########################################

# A short hand for loop that will print all items in a list:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
