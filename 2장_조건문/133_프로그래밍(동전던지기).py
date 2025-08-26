# 동전 던지기 게임
import random

print("동전 던지기 게임 시작!")
num = random.randrange(2)  # 0이나 1을 랜덤으로

if num == 0:
    print("동전이 앞면입니다.")
else:
    print("동전이 뒷면입니다.")

print("동전 던지기 게임을 종료합니다.")