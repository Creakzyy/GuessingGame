import random

n = random.randint(0,100)

c = 0

while True:
    c = c+1
    print("I am thinking of a number from 1-100, can you guess what it is?")
    g = int(input())
    
    if g == n:
        print("Your are correct!")
        print("You took", c, " guesses!")

    elif g<n:
        print("Too Low. Try Again.")
    
    else:
        print("Too High. Try Again.")