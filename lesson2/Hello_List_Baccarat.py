import random

# ♠	♥ ♦ ♣
poker1 = ['♠A', '♠2', '♠3', '♠4', '♠5', '♠6', '♠7', '♠8', '♠9', '♠10', '♠J', '♠Q', '♠K']
poker2 = ['♥A', '♥2', '♥3', '♥4', '♥5', '♥6', '♥7', '♥8', '♥9', '♥10', '♥J', '♥Q', '♥K']
poker3 = ['♦A', '♦2', '♦3', '♦4', '♦5', '♦6', '♦7', '♦8', '♦9', '♦10', '♦J', '♦Q', '♦K']
poker4 = ['♣A', '♣2', '♣3', '♣4', '♣5', '♣6', '♣7', '♣8', '♣9', '♣10', '♣J', '♣Q', '♣K']

poker = poker1 + poker2 + poker3 + poker4

random.shuffle(poker)  # 洗牌
print(poker)
balance = 10000 # 資金
index = 0 # poker init idex
while True:
    bet = int(input('下注 : $'))
    if(bet == 0) :
        break # 離開 while 迴圈
    betting = int(input('押 0:合, 1:莊, 2:閒 : '))

    bankerSum = 0 # 莊家
    playerSum = 0 # 莊家

    # 莊---------------------------------------------------------
    for item in poker[index:index+2]:
        num = item[1:len(item)] # A J Q K 2~10
        if num.isdigit(): # 2~10
            bankerSum += int(num)
        elif num == 'A':
            bankerSum += 1
        elif num == 'J' or num == 'Q' or num == 'K':
            bankerSum += 0

    bankerSum = bankerSum % 10
    index += 2 # 移動 index
    # 閒---------------------------------------------------------
    for item in poker[index:index+2]:
        num = item[1:len(item)] # A J Q K 2~10
        if num.isdigit(): # 2~10
            playerSum += int(num)
        elif num == 'A':
            playerSum += 1
        elif num == 'J' or num == 'Q' or num == 'K':
            playerSum += 0
    playerSum = playerSum % 10
    index += 2  # 移動 index
    # 計算---------------------------------------------------------

    winerStr = '合'
    winerNo = 0

    if bankerSum > playerSum:
        winerStr = '莊'
        winerNo = 1
    elif bankerSum < playerSum:
        winerStr = '閒'
        winerNo = 2

    if(winerNo == betting):
        balance += bet
    else:
        balance -= bet

    print('(%s) -> 莊家%s %d 點 閒家%s %d 點' % (winerStr, poker[index-4:index-2], bankerSum, poker[index-2:index], playerSum))
    print('balance $%d' % balance)
print('Game Over !')