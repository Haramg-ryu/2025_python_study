# BMI 게산기임. 사용자로부터 신장/체중을 입력받아서 BMI값에 따라 다음과 같은 메세지를 출력하는 프로그램 작성해
# 20~24.9 = 정상입니다 / 25~29.9 = 과체중입니다. / 30~ 비만입니다

height, weight = eval(input("키, 몸무게를 입력하세요 (170, 70) : "))
BMI = weight / ((height / 100) ** 2)

if 20 <= BMI <= 24.9:
    bmi_result = "정상입니다."
elif 25 <= BMI <= 29.9:
    bmi_result = "과체중입니다."
elif 30 <= BMI:
    bmi_result = "비만입니다."
else:
    bmi_result = "저체중입니다"

print(f"몸무게(kg) : {weight}\n키(cm) : {height}\n당신의 BMI : {BMI}\n{bmi_result}")