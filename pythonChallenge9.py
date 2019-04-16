import random

guessedNumber = 0
randomNumber = random.randrange(0,10)
exitCommand = "exit"

counter = 0

while guessedNumber != exitCommand and guessedNumber != randomNumber:

    guessedNumber = input("Guess a number between 1-9: ")
    guessedNumber = int(guessedNumber)
    counter = counter + 1
    
    if guessedNumber > randomNumber:
        print("The number you have chosen is to high. Try again: ")
    elif guessedNumber < randomNumber:
        print("The number you have chosen is to low. Try again: ")
    else:
        print("You have guessed the correct number in " , counter, " tries.")

    if guessedNumber == exitCommand:
        exit
