# 사용자로부터 키를 입력받아 표준체중을 계산한 후 사용자의 체중과 비교하여 저체중인지/표준인지/과체중인지 판단하는 프로그램 작성
# 표준체중 = (키-100) * 0.9

height, weight = eval(input("키와 몸무게를 입력해주세요 : "))
standard_weight = (height - 100) * 0.9

if weight == standard_weight:
    print("표준 체중입니다.")
elif weight < standard_weight:
    print("저체중 입니다.")
else:
    print("과체중 입니다.")