import random

# ♠	♥ ♦ ♣
poker1 = ['♠A', '♠2', '♠3', '♠4', '♠5', '♠6', '♠7', '♠8', '♠9', '♠10', '♠J', '♠Q', '♠K']
poker2 = ['♥A', '♥2', '♥3', '♥4', '♥5', '♥6', '♥7', '♥8', '♥9', '♥10', '♥J', '♥Q', '♥K']
poker3 = ['♦A', '♦2', '♦3', '♦4', '♦5', '♦6', '♦7', '♦8', '♦9', '♦10', '♦J', '♦Q', '♦K']
poker4 = ['♣A', '♣2', '♣3', '♣4', '♣5', '♣6', '♣7', '♣8', '♣9', '♣10', '♣J', '♣Q', '♣K']

poker = poker1 + poker2 + poker3 + poker4
'''
print(poker)
print('\033[90m' + str(poker))
print('\033[91m' + str(poker))
print('\033[92m' + str(poker))
print('\033[93m' + str(poker))
print('\033[94m' + str(poker))
print('\033[95m' + str(poker))
'''
random.shuffle(poker)  # 洗牌
for item in poker[:5]:
    if item.__contains__('♥') or item.__contains__('♦'):
        print('\033[91m' + item)
    else:
        print('\033[99m' + item)
