# 사용자로부터 3개의 정수를 읽어 들인 후 if-else 문을 사용해 가장 작은 값을 결정하는 프로그램 작성하라

a, b, c = eval(input("3개의 정수를 입력하세요 : "))

smallest = a  # 처음엔 a가 제일 작다고 가정

# b랑 비교
if b < smallest:
    smallest = b
else:
    smallest = smallest  # 그대로 둠

# c랑 비교
if c < smallest:
    smallest = c
else:
    smallest = smallest  # 그대로 둠

print(f"제일 작은 정수는 {smallest}입니다.")
