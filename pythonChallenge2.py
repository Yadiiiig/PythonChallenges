number = input("Give a random number: ")
number = int(number)


def oddOrNah(randomNumber):
    calc = randomNumber % 2
    if (calc == 0):
        print("This number is even")
    elif (calc == 1):
        print("This number is odd")

oddOrNah(number)