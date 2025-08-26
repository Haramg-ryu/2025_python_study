# 배송지 : 한국 / 2만원 이상 무료 / 2만원 이하 3000원
# 배송지 : 미국 / 10만원 이상 무료 / 10만원 이하 8000원

country = input("국가를 입력하세요 (한국/미국) : ")
price = int(input("상품 가격을 입력하세요 : "))

# 한국/미국에 따른 조건문
if country == "한국":
    if price >= 20000:
        delivery = 0
    else:
        delivery = 3000
elif country == "미국":
    if price >= 100000:
        delivery = 0
    else:
        delivery = 8000

# 총 구매금액
total = price + delivery

print(f"배달 국가 : {country} / 구매금액 : {price:,} / 배송비 : {delivery:,}\n총 결제금액 : {total:,}")