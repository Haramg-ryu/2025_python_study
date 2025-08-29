# 별모양 계단을 만들자. 중첩 반복문을 활용한다.

# 알고리즘
# 별 하나를 생성한다.
# 별이 하나씩 증가되는 구문을 반복한다.

for i in range(1, 6):
    for j in range(i):  # i만큼 반복한다
        print("*", end="")
    print("")


# 우측정렬된 별 ==================================
n = 5  # 5줄
for i in range(1, n+1):
    for j in range(n-i):  # i만큼 반복한다
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print("")


# 우측정렬된 별 ==================================
n = 5  # 줄 수

for i in range(1, n+1):          # 1 ~ 5
    print(" " * (n - i) + "*" * i)
