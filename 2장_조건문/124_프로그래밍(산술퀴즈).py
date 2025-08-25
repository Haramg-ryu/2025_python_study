# 초등학생들을 위한 산수 퀴즈를 발생시키는 프로그램을 작성 (+, -, *, / 사용하자.)

import random

x = random.randint(1, 100)
y = random.randint(1, 100)
mark = random.choice(['+', '-', '*', '/'])

# 문제를 내자.
if mark == '+':
    st_answer = int(input(f"{x} + {y} = "))
    answer = x + y

elif mark == '-':
    st_answer = int(input(f"{x} - {y} = "))
    answer = x - y

elif mark == '*':
    st_answer = int(input(f"{x} * {y} = "))
    answer = x * y

elif mark == '/':
    st_answer = int(input(f"{x} / {y} = "))
    answer = x / y


# 정답 확인
flag = answer == st_answer
print(flag)


if flag == False:
    print(f"땡! 틀렸습니다.\n정답은 {x} {mark} {y} = {answer}")

else:
    print("정답입니다!")