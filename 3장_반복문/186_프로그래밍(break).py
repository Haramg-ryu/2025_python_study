# 무한루프의 break, continue

while True:
    light = input("신호등 색상을 입력하세요 : ").lower()
    if light == "green":
        break
print("전진!")