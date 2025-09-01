# 다음 리스트에 저장된 정수들의 합을 계싼하는 프로그램을 작성해보자. 내장함수 sum()은 이용하지 않는다.

my_List = [ 11, 22, 23, 99, 81, 93, 35 ]

total = 0

for i in my_List:
    total += i
print(f"정수들의 합 : {total}")