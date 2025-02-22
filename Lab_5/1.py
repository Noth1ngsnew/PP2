import re

txt = input("Enter sentence: ")
x = re.findall("ab*", txt)
print(x)