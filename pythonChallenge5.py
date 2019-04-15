import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

randomList1 = random.sample(range(60), 10)
randomList2 = random.sample(range(60), 10)
newList = []

for x in a:
    if x in b and x not in c:
        c.append(x)

for y in randomList1:
    if y in randomList2 and y not in newList:
        newList.append(y)

print(c)
print(newList)