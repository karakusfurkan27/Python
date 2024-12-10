import random
randomNumber = random.randint(1, 5)
guessCount = 0
guessLimit = 3
while guessCount < guessLimit:
    guess = int (input("Enter your guess:"))
    guessCount += 1
    if guess == randomNumber:
        print("You won!")
        break

else:
    print("Sorry, you failed!")