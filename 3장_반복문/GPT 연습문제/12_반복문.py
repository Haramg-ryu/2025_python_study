# 문제 4. (⭐⭐⭐)

# 0도부터 180도까지 30도 간격으로 tan 값을 출력하는 프로그램을 작성하시오.
# 출력은 각도, tan 두 열로 정렬해서 나타낼 것.
# math.tan() 사용.

import math

print("   각도     tan    ")
print("--------------------")

for degree in range(0, 181, 30):
    radian = 3.14 * degree / 180.0
    tan = math.tan(radian)
    print(f"{degree:3d} {tan:7.3f}")