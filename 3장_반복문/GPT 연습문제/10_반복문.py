# 문제 2. (⭐⭐)

# 1부터 n까지의 홀수의 합만 구하는 프로그램을 작성하시오.
# 예: n=10 → 1+3+5+7+9 = 25

num = int(input("정수를 입력하세요 : "))

total = 0

for i in range(1, num + 1):
    if i % 2 != 0:
        total += i
print(total)