playerOneReady = False
playerTwoReady = False

playerOne = input("Player One: What do you pick? Rock, Paper or Scissors? ")

if (playerOne == "Rock" or playerOne == "Paper" or playerOne == "Scissors"):
    playerOneReady = True
else:
    print("Error, you chose something wrong.")

playerTwo = input("Player Two: What do you pick? Rock, Paper or Scissors? ")

if (playerTwo == "Rock" or playerTwo == "Paper" or playerTwo == "Scissors"):
    playerTwoReady = True
else:
    print("Error, you chose something wrong.")

def rockPaperScissors(first, second):
    if first == "Rock":
        if second == "Rock":
            print("Tied!")
        elif second == "Paper":
            print("Player Two wins!")
        elif second == "Scissors":
            print("Player One wins!")
    elif first == "Paper":
        if second == "Rock":
            print("Player One wins!")
        elif second == "Paper":
            print("Tied!")
        elif second == "Scissors":
            print("Player Two wins!")
    elif first == "Scissors":
        if second == "Rock":
            print("Player Two wins!")
        elif second == "Paper":
            print("Player One wins!")
        elif second == "Scissors":
            print("Tied!")

rockPaperScissors(playerOne, playerTwo)