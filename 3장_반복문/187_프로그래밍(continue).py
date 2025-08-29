# Continue 프로그램
# 1부터 10까지 중엣 3의 배수만 빼고 출력해보자.

for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i, end=" ")