import random

hidden = random.randrange(1, 6)

guess = int(input("Please enter your guess:"))

if guess == hidden:
    print( "You guess right!")
elif guess < hidden:
    print("Your guess is too low")

else:
    print("Your guess is too high")

print(hidden)