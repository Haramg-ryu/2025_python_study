# 연도를 입력하면 띠를 출력하는 프로그램 작성
# 띠는 연도를 12로 나누어서 결정됨. 나머지가 0=원숭이, 1=닭띠 2=개띠

year = int(input("연도를 입력하세요 : "))
year_12 = year % 12

if year_12 == 0:
    ddi = "원숭이띠"
elif year_12 == 1:
    ddi = "닭띠"
elif year_12 == 2:
    ddi = "개띠"
elif year_12 == 3:
    ddi = "돼지띠"
elif year_12 == 4:
    ddi = "쥐띠"
elif year_12 == 5:
    ddi = "소띠"
elif year_12 == 6:
    ddi = "호랑이띠"
elif year_12 == 7:
    ddi = "토끼띠"
elif year_12 == 8:
    ddi = "용띠"
elif year_12 == 9:
    ddi = "뱀띠"
elif year_12 == 10:
    ddi = "말띠"
elif year_12 == 11:
    ddi = "양띠"

print(f"{year}년은 {ddi} 입니다.")
