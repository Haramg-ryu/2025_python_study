# 숫자 맞추기 게임
import random

print("1부터 100 사이의 숫자를 맞추세요.")
print("===============================")

# 컴퓨터가 숫자를 선택합니다.
com_num = random.randint(1, 100)
count = 0

# 유저가 숫자를 맞추기 시작합니다. (카운트)
while True:
    user_num = int(input("숫자를 입력하세요 : "))
    count += 1  # 카운트

    if com_num == user_num:
        print(f"정답! {count}번 만에 맞추었습니다.")
        break

    elif com_num < user_num:
        print(f"숫자를 내리세요!")
    elif com_num > user_num:
        print(f"숫자를 올리세요!")