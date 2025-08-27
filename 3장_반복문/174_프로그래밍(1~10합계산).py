# 1과 10까지의 합 계산하기

num = int(input("어느 숫자까지 더할지 적으시오 : "))
sum = 0
i = 1

while i <= num:
    sum = i + sum   # 합계 누적
    i = i + 1       # 다음 숫자로 이동하여 while 다시 ㄱㄱ

print(f"{num}까지 더한 값은 {sum}")