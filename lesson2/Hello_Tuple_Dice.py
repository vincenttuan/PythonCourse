import random
dice = (1, 2, 3, 4, 5, 6)  # 骰子
amount = 3  # 骰子數量
balance = 10000  # 初始金額

while True:
    bet = int(input('下注 : $'))
    if (bet == 0):
        break  # 離開 while 迴圈
    betting = int(input('押 0:小, 1:大 : '))
    sum = 0  # 點數總和
    sum_betting = 0  # 點數總和指數
    for n in range(0, amount):
        i = random.randrange(0, len(dice))  # 0~5
        print("第{}顆骰子:i={} -> dice[{}]={}".format(n+1, i, i, dice[i]))
        sum += dice[i]

    if sum >= 10 :
        sum_betting = 1
    else :
        sum_betting = 0

    if sum_betting == betting :
        balance += bet
    else :
        balance -= bet

    print("開 {} 總和={} 餘額 ${}".format('大' if sum>10 else '小', sum, balance))

