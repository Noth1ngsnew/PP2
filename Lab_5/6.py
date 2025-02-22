import re

txt = input("Enter sentence: ")
x = re.sub(r"[ ,.]", ":", txt)
if x:
    print(x)
else:
    print("No match")