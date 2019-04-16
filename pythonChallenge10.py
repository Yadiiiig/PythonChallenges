import random

randomList1 = random.sample(range(60), 10)
randomList2 = random.sample(range(60), 10)

comperhension = [x for x in randomList1 if x in randomList2]
print(comperhension)