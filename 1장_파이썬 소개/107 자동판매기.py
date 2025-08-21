price = int(input("물건 값을 입력하세요. : "))
print("")

print("===입력금액===")
note = int(input("1000원 지폐 개수 : "))
Coin500 = int(input("500원 동전 개수 : "))
Coin100 = int(input("100원 동전 개수 : "))

change = note * 1000 + Coin500 * 500 + Coin100 * 100 - price



c_note = change//1000
change = change%1000

c_Coin500 = change//500
change = change%500

c_Coin100 = change//100
change = change%100

c_Coin50 = change//50
change = change%50

c_Coin1 = change

print("==거스름돈 출력==")
print(f"1000원 = {c_note}, 500원 = {c_Coin50}, 100원 = {c_Coin100}, 50원 = {c_Coin50}, 1원 = {c_Coin1}")
