# 사용자가 입력한 정수의 모든 약수를 화면에 출력하는 프로그램을 작성하라.

# num = int(input("약수를 구할 정수를 입력하시오 : "))

# print(f"{num}의 약수 : ")

# for i in range(1, num + 1):
#     if num % i == 0:
#         print(i, end=" ")


# ----------------------------------------------------------------
# while문

num = int(input("약수를 구할 정수를 입력하시오 : "))

print(f"{num}의 약수 : ")

i = 1

while i <= num:
    if num % i == 0:
        print(i, end=" ")
    i += 1