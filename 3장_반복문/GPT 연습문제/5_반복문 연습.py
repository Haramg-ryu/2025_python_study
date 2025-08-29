# 1부터 10까지 숫자 중에서 짝수만 출력하시오.
# 👉 for문으로 풀기, while문으로 풀기 두 가지 버전 다 시도해봐.

# for문
for i in range(1, 11):
    if i % 2 == 0:
        print(f"for 짝수 : {i}")


# while문
i = 0

while i <= 10:
    i += 1
    if i % 2 == 0:
        print(f"while 짝수 : {i}")