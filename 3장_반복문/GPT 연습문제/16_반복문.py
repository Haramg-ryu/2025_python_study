# 문제 3. (⭐⭐⭐)

# 중첩 반복문을 사용하여 다음과 같이 출력하시오.

# *****
# ****
# ***
# **
# *

num = int(input("숫자를 입력하세요 : "))

for i in range(num, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# ----------------------------------------

# num = int(input("숫자를 입력하세요 : "))

# i = num


# while i > 0:
#     j = 0
#     while j < i:
#         print("*", end=" ")
#         j += 1
#     print()
#     i -= 1
    