# 사용자가 리히터 규모를 입력하면 피해 정도를 출력하는 프로그램을 작성해보자.
# 0~2 규모 : 큰 피해 없음
# 3~4 규모 : 일부 지역 피해 있음
# 5~6 규모 : 일부 지역 큰 피해가 있음
# 7~8 규모 : 주변 지역까지 큰 피해가 있음
# 9이상 규모 : 여진 지역까지 매우 큰 피해가 있음

richter = float(input("리히터 규모를 입력하시오 : "))

if richter <= 2:
    print(f"📢현재 지진 규모 [{richter:.2f}]. 큰 피해 없음.")
elif richter <= 4:
    print(f"📢현재 지진 규모 [{richter:.2f}]. 일부 지역 피해 있음")
elif richter <= 6:
    print(f"📢현재 지진 규모 [{richter:.2f}]. 일부 지역 큰 피해가 있음")
elif richter <= 8:
    print(f"📢현재 지진 규모 [{richter:.2f}]. 주변 지역까지 큰 피해가 있음")
else:
    print(f"📢현재 지진 규모 [{richter:.2f}]. 여진 지역까지 매우 큰 피해가 있음")