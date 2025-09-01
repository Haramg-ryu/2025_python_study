# 문제 4. (⭐⭐⭐)

# 컴퓨터가 1부터 50 사이의 랜덤 정수를 하나 선택한다.
# 사용자는 계속 입력하면서 맞추어야 한다.

# 입력한 숫자가 크면 "DOWN",
# 작으면 "UP",
# 같으면 "정답!" 출력 후 종료.
# 👉 while문을 사용하시오.

# ------------------------------------------------

import random

com_num = random.randint(1, 50)

while True:
    user_num = int(input("컴퓨터의 숫자는 무엇일까요? : "))

    if com_num == user_num:
        print("정답입니다!")
        break
    elif com_num > user_num:
        print("UP")
    elif com_num < user_num:
        print("DOWN")