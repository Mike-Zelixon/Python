import random

secretNum = random.randint(1,20)
print("I'm thinking of a # between 1 and 20")

#Ask the player for 6 guesses

count = 5
for guessesTaken in range(5):

    guess = int(input("Take a guess: "))

    if guess < secretNum:
        print("Too low!", end=' ')
        count -= 1
        print("You have " +str(count)+ " guesses left")
    elif guess > secretNum:
        print("Too high!", end=' ')
        count -= 1
        print("You have " + str(count) + " guesses left")
    else:
        break

if guess == secretNum:
    print("Congrats! It took you " + str(guessesTaken) + " times to guess the number :) ")
else:
    print("Sorry, the correct number was " +str(secretNum))


