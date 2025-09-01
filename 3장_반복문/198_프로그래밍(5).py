# 중첩 반복문을 사용하여 다음과 같이 출력하라

# num = int(input("정수를 입력하세요 : "))

# for i in range(1, num + 1):
#     for j in range(1, i):
#         print(j, end=" ")
#     print()


num = int(input("정수를 입력하세요 : "))

i = 1

while i <= num:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1
