# 다음과같이 0도부터 90도까지 10도 간격으로 sin값과 cos값 출력하는 프로그램을 작성

# sin = c/a
# cos = b/a
# tan = c/b

import math

print("각도   sin값    cos값")   # 제목 출력
print("----------------------")

for degree in range (0, 91, 10):
    radian = 3.14 * degree / 180.0
    s = math.sin(radian)
    c = math.cos(radian)
    print(f"{degree:3d}{s:9.3f}{c:9.3f}")