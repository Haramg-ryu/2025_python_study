# for문을 이용한 팩토리얼 계산

num = int(input("팩토리얼의 마지막 숫자를 입력하세요 : "))
# 1*2*3*4*5*...100
fact = 1  # 1부터 시작! 0이면 전체 값이 0이 됨

for i in range (1, num+1):  # 마지막 숫자는 +1 해주고
    fact = fact * i
print(num,"!은", fact, "이다.")