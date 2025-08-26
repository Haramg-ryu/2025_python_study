# 본문에서 덧셈퀴즈를 자동으로 생성함. 덧/뺄/곱/나눗셈중 하나를 랜덤하게 선택하고, 피연산자도 난수로 생성하여 사용자에게 제시하고
# 사용자의 답을 자동으로 채점하는 프로그램을 작성

import random

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)

# 랜덤으로 초이스
mark = random.choice(["+", "-", "*", "/"])

user_answer = float(input(f"{num1} {mark} {num2}  답은?"))

if mark == "+":
    answer = num1 + num2
elif mark == "-":
    answer = num1 - num2
elif mark == "*":
    answer = num1 * num2
elif mark == "/":
    answer = num1 / num2

if user_answer == answer:
    print("정답입니다!")
else:
    print("땡! 틀렸습니다")