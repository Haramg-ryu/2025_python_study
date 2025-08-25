# 상품 세일 가격을 계산하는 프로그램 개발.
# 점원이 원래 가격 입력하면 우리 프로그램은 할인된 가격을 출력
# 100만원 미만 = 10% 할인 적용 : 사은품 없음
# 100만원 이상이면 15% 할인 적용 : 사은품 있음

price = int(input("정가를 입력하세요 : "))

if price >= 1000000:
    sale_percent = 15
    print(f"구매금액 : {price:,}원\n사은품을 지급해주세요.")

else:
    sale_percent = 10
    print(f"구매금액 : {price:,}원\n사은품 없음")

# 할인가 계산
sale = price * (1 - (sale_percent / 100))

print(f"할인된 제품 가격 : {sale:,.0f}원")