# 투자금이 2배가 되는 걸리는 시간 계산
TARGET = 2000
money = 1000   # 투자금액 초기자본
year = 0       # 연도 초기화
rate = 0.07    # 이자율

while TARGET > money:
    money = money + money * rate  # 돈 + 이자 증정
    year = year + 1

print(year, "년")