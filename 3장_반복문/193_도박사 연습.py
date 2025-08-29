# 미니버전 : 한판만 하기

import random

cash = 5
goal = 10

while cash > 0 and goal:
    number = random.randint(1, 2)  # 이기고/지고
    if number == 1:
        cash = cash + 1
    else:
        cash = cash - 1
    print("현재 돈 : ", cash)

if cash == goal:
    print("목표 달성")
else:
    print("돈 다 잃음...")