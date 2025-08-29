# 2개의 주사위를 던져 6이 나올 확률은 5/36이다. 
# 1000번의 가상적인 주사위를 던진 후에 6이 나오는 횟수를 세어 이론적인 확률값과 비교하는 프로그램 작성

import random

TRIALS = 1000
count = 0

for _ in range (TRIALS):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    if dice1 + dice2 == 6:
        count += 1

# 실험적 확률
experimental_prob = count / TRIALS

# 확률
prob = 5 / 36

print(f"1000번 던진 결과, 합이 6인 경우는 {count}번")

print(f"실험적 확률 = {experimental_prob:.4f}")
print(f"이론적 확률 = {prob:.4f}")
