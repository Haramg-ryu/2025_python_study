# 사용자로부터 온도를 입력받아 현재 물의 상태를 출력하는 프로그램

celcius = float(input("물 온도를 입력하세요. (섭씨) : "))


if celcius <= 0:
    water_state = "고체"
elif celcius > 0 and celcius <= 100:
    water_state = "액체"
elif celcius > 100:
    water_state = "기체"

print(f"현재 물 온도 : {celcius} / 물 상태 : {water_state}")