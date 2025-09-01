# while 루프를 이용해서 n^2 500인 n중에서
# 가장 작은 n을 찾는 프로그램 작성

i = 1

while True:
    if i **2 >= 500:
        print(f"가장 작은 n : {i}")
        break    
    i += 1