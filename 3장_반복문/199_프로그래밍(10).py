# 1^2 + 2^2 + 3^2 + ... n^2의 값을 계산하여
# 출력해보자. n의값 받고, 계산값을 출력한다.
# 10을 받으면 385가 출력된다.

n = int(input("정수를 입력하세요 : "))

total = 0

for i in range (1, n + 1):
    total += i ** 2
print(total)