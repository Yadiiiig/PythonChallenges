newList = []
numberInput = input("Please choose a number to divide: ")
numberInput = int(numberInput)
firstList = list(range(1, numberInput + 1))

for x in firstList:
    if numberInput % x == 0:
        newList.append(x)

print(newList)