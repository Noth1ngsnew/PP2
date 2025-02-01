def solve(numheads, numlegs):
    rabbits = (numlegs - 2 * numheads) / 2
    chickens = numheads - rabbits
    print (rabbits, chickens)

        
heads = int(input("Heads: "))
legs = int(input("Legs: "))
solve(heads,legs)