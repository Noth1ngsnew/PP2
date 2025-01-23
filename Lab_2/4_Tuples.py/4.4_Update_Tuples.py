#Packing a tuple:
fruits = ("apple", "banana", "cherry")

#####################################################

#Unpacking a tuple:
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

########################################################
'''
If the number of variables is less than the number of values, 
you can add an * to the variable name and the values will be 
assigned to the variable as a list:
'''
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

###############################################################

#Add a list of values the "tropic" variable:
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
