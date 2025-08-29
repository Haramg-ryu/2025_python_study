number = 2   # 소수 검사는 2부터 시작

while number <= 100:
    divisor = 2
    prime = True

    while divisor < number:
        if number % divisor == 0:
            prime = False
            break
        divisor += 1   # ← 이게 while 안쪽에 있어야 함!

    if prime:
        print(number, end=" ")
    
    number += 1
