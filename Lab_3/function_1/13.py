import random
def random_number(name):
    i = 1
    r = random.randint(1,20)
    while(True):
        num = int(input("Take a guess: "))
        if num == r:
            print(f"Good job, {name}! You guessed my number in {i} guesses!")
            break
        elif num>r:
            print("Your guess is too high.")
            i+=1
        else:
            print("Your guess is too low")
            i+=1
            

a = input("Hello! What is your name?")
print(f"Well,{a}, I am thinking of a number between 1 and 20.")
random_number(a)

