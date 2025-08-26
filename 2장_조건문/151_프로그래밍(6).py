# 가위바위보 프로그램 작성. 컴퓨터는 사용자에게 알리지 않고 가위/바위/보 중에서 임의 하나 선택
# 사용자는 프로그램의 입력 안내 메세지에 따라서 3개 중 하나를 선택하게 된다
# 사용자의 선택이 끝나면 컴퓨터는 누가 무엇을 선택하였고 누가 이겼는지/비겼는지 알려준다ㅏ.

import random

print("가위 바위 보 시작!")
computer = random.randint(1, 3)
user = int(input("컴퓨터는 골랐습니다. 무엇을 고르시겠어요? (1: 가위/ 2: 바위/ 3: 보) : "))

names = {1: "가위", 2: "바위", 3: "보"}

print(f"당신은 {names[user]}을 냈습니다.")
print(f"컴퓨터는 {names[computer]}을 냈습니다.")

if user == computer:
    print("비겼습니다!")
elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
    print("이겼습니다!")
else:
    print("졌습니다!")