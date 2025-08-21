weight = float(input("몸무게를 kg단위로 입력하시오 (ex. 45.0) : "))
height = float(input("키를 미터(m) 단위로 입력하시오 (ex. 1.75) : "))

BMI = (weight / (height**2))
print(f"당신의 BMI는 {BMI:.2f} 입니다.")



# 키를 센치미터로 받아서 미터로 변환
weight = float(input("몸무게를 kg단위로 입력하시오 (ex. 45.0) : "))
height = float(input("키를 센치미터(cm) 단위로 입력하시오 (ex. 175.0) : "))

height_m = height * 0.01
BMI = (weight / (height_m**2))
print(f"당신의 BMI는 {BMI:.2f} 입니다.")