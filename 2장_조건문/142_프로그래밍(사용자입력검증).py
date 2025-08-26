# 메뉴번호가 1~3이 있는 상점에서 사용자가 반드시 1~3사이에서 선택해야함.
# 검증하지 않고 넘어가게 되면 오류메세지를 출력한다.

print("==========================")
print("메뉴 1번 : 치즈버거")
print("메뉴 2번 : 치킨버거")
print("메뉴 3번 : 불고기 버거")
print("==========================")

menu = int(input("메뉴를 선택하세요 : "))

if menu >= 1 and menu <= 3:
    if menu == 1:
        burger = "치즈버거"
    elif menu == 2:
        burger = "치킨버거"
    elif menu == 3:
        burger = "불고기 버거"
    print(f"메뉴 {menu}번 : {burger}")
else:
    print("잘못 입력하셨습니다.")