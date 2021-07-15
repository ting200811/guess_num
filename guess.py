# 猜數字練習
import random
r = random.randint(1, 100)

while True:
    num = input('請猜猜看數字')
    num = int(num)
    if num == r:
        print('棒毆')
        break
    elif num > r:
        print('比答案大')
    elif num < r:
        print('比答案小')