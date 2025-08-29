# 리스트의 반복

fruit = ["사과", "바나나", "멜론", "수박"]
vega = ["상추", "배추", "궁채", "양배추"]

for i in fruit:
    for j in vega:
        print(i, j)



for i in range(1,3):
    for j in range(1,3):
        print(i, "곱하기", j, "는", i*j)