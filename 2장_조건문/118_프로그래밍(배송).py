# 배송비 계산 프로그램

price = int(input("구매 금액을 입력해주세요 : "))

if price >= 30000:
    shipping_cost = 0
else:
    shipping_cost = 3000

print(f"총 구매금액 : {price}원\n배송비 : {shipping_cost}")