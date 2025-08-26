# 다음의 조건에 해당하는 논리 연산식을 만들고, 변수는 적절하게 선언되어있다고 가정
# 나이는 25살 이상, 연봉은 3500만원 이상

name = input("이름을 입력하세요 : ")
age = int(input("나이를 입력하세요 : "))
money = int(input("연봉을 입력하세요 : "))

if age >= 25 and money >= 3500:
    get_through = "합격"
else:
    get_through = "불합격"

print(f"이름 : {name} / 나이 : {age} / 연봉 : {money}\n결과 : {get_through}")