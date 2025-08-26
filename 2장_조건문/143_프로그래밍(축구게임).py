# 난수를 이용하여 간단한 축구게임을 작성.
# 사용자가 컴퓨터를 상대로 패널티킥을 한다고 생각.
# 다음의 3가지 영역 중 하나를 선택하여 패널티킥을 한다
# 컴퓨터도 난수를 생성하여 3개의 영역 중 하나를 수비한다.

# 어디를 수비하시겠어요? (왼쪽:1, 중앙2, 오른쪽 3)

import random

computer_choice = random.randint(1,3)
user_choice = int(input("어디를 수비하시겠어요? (왼쪽:1, 중앙2, 오른쪽 3) : "))

if computer_choice == user_choice:
    print("수비에 성공하였습니다!")
else:
    print("수비에 실패하였습니다. 패널티킥 성공!")