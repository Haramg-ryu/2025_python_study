# 성적 90이상 A / 80이상 90미만 B / 70이상 80미만 C, 이외 F

print("===학점 계산기===")

score = int(input("점수를 입력하세요 : "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print("=================")
print(f"점수 : {score} / 학점 : {grade}")