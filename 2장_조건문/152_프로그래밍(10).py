# 다음과 같이 정의되는 함수의 함수값을 계산하여 보자. 사용자로부터 x값을 입력 받아서 합수값을 계산하여 화면에 출력. x는 실수.

x = float(input("x의 값을 입력하시오 : "))

if x <= 0:
    total = (x ** 2) - (9 * x) + 2
elif x >= 0:
    total = (7 * x) + 2

print(f"f(x)의 값은 {total:6f}")