# 조건 연산자를 활용하여 변수 age가 21세 미만이면 minor, 그렇지 않으면 adult

age = int(input("나이를 입력하세요 : "))

age_confirm = ("adult" if age >= 21 else "minor")
print(age_confirm)