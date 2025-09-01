# 어떤 사람이 100원짜리 동전 5개(=500원) 을 가지고 있다.
# 한 번에 70원씩 쓰면서 물건을 산다.
# 돈이 0원 이하가 되면 멈추고,
# 그 과정에서 "남은 돈 = ?" 을 출력하는 프로그램을 작성하시오.

coins = 5
coin = 100 * coins

while coin > 0:
    coin -= 70
    if coin < 0:
        continue
    print(f"남은 돈 = {coin}")

