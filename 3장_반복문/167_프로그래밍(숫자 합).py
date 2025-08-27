# 1부터 n까지의 합 계산

num = int(input("합계를 구할 수를 기재하시오(마지막 수) : "))
sum = 0

for n in range (1, 1 + num):
    sum = sum + n
print(f"합 : {sum}")