# 문제 1. (⭐)

# 1부터 n까지의 합을 구하는 프로그램을 작성하시오.
# 예: n=10 → 55

n = int(input("정수를 입력하세요 : "))

total = 0

for i in range(1, n + 1):
    total += i
print(f"합 : {total}")
