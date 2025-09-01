# 문제 3. (⭐⭐)

# 중첩 반복문을 사용하여 아래와 같이 출력하시오. (계단 모양)

# 1
# 12
# 123
# 1234
# 12345


for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()