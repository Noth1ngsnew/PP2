def palindrome(word):
    if(word  == word[::-1]):
        print(True)
    else:
        print(False)

word = input("Enter word or sentence: ")
palindrome(word)
