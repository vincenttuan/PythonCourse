import random

# ♠	♥ ♦ ♣
poker1 = ['♠A', '♠2', '♠3', '♠4', '♠5', '♠6', '♠7', '♠8', '♠9', '♠10', '♠J', '♠Q', '♠K']
poker2 = ['♥A', '♥2', '♥3', '♥4', '♥5', '♥6', '♥7', '♥8', '♥9', '♥10', '♥J', '♥Q', '♥K']
poker3 = ['♦A', '♦2', '♦3', '♦4', '♦5', '♦6', '♦7', '♦8', '♦9', '♦10', '♦J', '♦Q', '♦K']
poker4 = ['♣A', '♣2', '♣3', '♣4', '♣5', '♣6', '♣7', '♣8', '♣9', '♣10', '♣J', '♣Q', '♣K']

poker = poker1 + poker2 + poker3 + poker4

random.shuffle(poker)  # 洗牌
sum = 0
for item in poker[:2]:
    num = item[1:len(item)] # A J Q K 2~10

    if num.isdigit(): # 2~10
        sum += int(num)
    elif num == 'A':
        sum += 11
    elif num == 'J' or num == 'Q' or num == 'K':
        sum += 10

    if item.__contains__('♥') or item.__contains__('♦'):
        print('\033[91m' + item)
    else:
        print('\033[99m' + item)

print('\033[99m' + str(sum))
