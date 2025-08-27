# 초등생을 위한 산수 문제를 발생시키는 프로그램이다. 한번이라도 틀리면 반복을 중단한다.
import random

while True:
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    mark = random.choice(["+", "-", "*", "/"])

    if mark == "+":
        answer = num1 + num2
    elif mark == "-":
        answer = num1 - num2
    elif mark == "*":
        answer = num1 * num2
    elif mark == "/":
        answer = num1 / num2

    user_answer = float(input(f"{num1} {mark} {num2} = "))

    if user_answer == answer:
        print("잘했어요!")
    else:
        print("틀렸어요. 하지만 다음에는 잘할 수 있죠?")
        break