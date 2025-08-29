# 문제 3. (⭐⭐⭐ 조금 응용)

# 컴퓨터가 1~100 사이의 랜덤 숫자를 하나 고른다.
# 사용자는 계속 숫자를 입력하면서 맞춰야 한다.

# 입력한 숫자가 크면 "DOWN"
# 작으면 "UP"
# 정답이면 "정답!" 출력하고 게임 끝.

# 👉 힌트: for문이 아니라 while문이 딱 맞음.

import random

count = 0
com_num = random.randint(1, 100)

while True:
    user_num = int(input("숫자를 입력해주세요 : "))

    count += 1

    if user_num == com_num:
        print("정답!")
        break
    elif user_num > com_num:
        print("DOWN")
    elif user_num < com_num:
        print("UP")
    

print(f"맞춘 시도 횟수 : {count}, 정답 : {com_num}")