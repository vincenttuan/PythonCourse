import random
dice = (1, 2, 3, 4, 5, 6)
i = random.randrange(0, len(dice)) # 0~5
print(str(i) + " -> " + str(dice[i]))
