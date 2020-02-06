# pages 74-76


# this is a guess the number game

import random

print('Hello what is your name?')
name = input()
secretNumber = random.randint(1,20)

print("hello " + name + ", I am thinking of anumber between 1 and 20")

# ask player to guess 6 times
for guessesTaken in range(1,7):
    print('take a guess what it is')
    guess = int(input())
    if guess < secretNumber:
        print('nice number but that was too low')
    elif guess > secretNumber:
        print('good guess but that is too high')
    else:
        print("YES THAT IS THE NUMBER GOOD GUESS")
        break

if guess == secretNumber:
    print("Good job, " + name + "! You guessed my number in just " + str(guessesTaken) + " guesses")
else:
    print("Well rats, SORRY there " + name + " the secret number was actually " + str(int(secretNumber)))
