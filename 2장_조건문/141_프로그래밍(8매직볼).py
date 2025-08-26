# 조건문을 활용하여 오늘의 운세를 알려주는 프로그램 개발.
# 난수를 발생하여서 난수에 해당하는 운세를 출력한다.

import random

print("오늘의 운세를 확인해보자!")
num = random.randrange(5)  # 0 1 2 3 4

if num == 0:
    lucky = "운세1 문장"
elif num == 1:
    lucky = "운세2 문장"
elif num == 2:
    lucky = "운세3 문장"
elif num == 3:
    lucky = "운세4 문장"
elif num == 4:
    lucky = "운세5 문장"

print(f"오늘의 운세 멘트 : {lucky}")

# 조건문 말고 리스트 -------------------------------

# import random

# print("오늘의 운세를 확인해보자!")

# lucky_list = [
#     "운세1 문장",
#     "운세2 문장",
#     "운세3 문장",
#     "운세4 문장",
#     "운세5 문장"
# ]

# lucky = random.choice(lucky_list)  # 리스트에서 하나 뽑기
# print(f"오늘의 운세 멘트 : {lucky}")
