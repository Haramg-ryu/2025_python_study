# 사용자로부터 pH 농도를 받아 "알칼리/산/중성" 나누어서 출력 ㄱㄱ

pH = float(input("pH 농도를 입력하세요 : "))

if 1 <= pH <= 6:
    print("산성입니다.")
elif pH == 7:
    print("중성입니다.")
elif 8 <= pH <= 14:
    print("알칼리 입니다.")
else:
    print("잘못된 입력값입니다. (1~14 사이)")