# 猜數字練習
import random
strat = input('請輸入範圍起始值: ')
end = input('請輸入範圍結束值: ')
strat = int(strat)
end = int(end)

r = random.randint(strat, end)
count = 0
while True:
    num = input('請猜猜看數字:')
    num = int(num)
    count += 1
    if num == r:
        print('棒毆')
        print('第', count,'次就猜到了')
        break
    elif num > r:
        print('比答案大')
    elif num < r:
        print('比答案小')
    print('您猜了', count, '次')