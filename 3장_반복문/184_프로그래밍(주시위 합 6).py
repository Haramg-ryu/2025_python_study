# 주사위 합이 6이 되는 경우를 전부 출력

for i in range(1, 7):
    for j in range(1, 7):
        if i + j == 6:
            print(f"(첫번째 주사위 : {i}, 두번째 주사위 : {j})")